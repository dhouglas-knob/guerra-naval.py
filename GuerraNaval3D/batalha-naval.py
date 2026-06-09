import moderngl
import os 
import pygame
import pyrr
import numpy as np
from PIL import Image

# Define camera class. Since  i plan on making this for a game where the player has minimal control of the camera i won't implement
# the necessary features for free camera mode such as calculating forward and right vectors
current_dir = os.getcwd()

class Camera3D:
    def __init__(self):
        self.translation = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0])) 
        self.rotation = pyrr.matrix44.create_from_x_rotation(0) @ pyrr.matrix44.create_from_y_rotation(0) @ pyrr.matrix44.create_from_z_rotation(0)
        self.perspective = pyrr.matrix44.create_perspective_projection_matrix(
        fovy= 45, 
        aspect= 1.6, 
        near= 0.1, 
        far= 1000
        )
        self.forwardvec = self.rotation[2][:3] # If you want to use the forward vector, its available
        # Sets the default values so that the camera can exist before you send any inputs to it
        prog['u_projection'].value = tuple(self.perspective.flatten())
        self.GetViewMatrix()
        
    def CameraPerspective(self, fov: int,aspect_ratio: int, nearZ:float,farZ:float) -> pyrr.matrix44:
        """Sets the camera perspective"""
        self.perspective = pyrr.matrix44.create_perspective_projection_matrix(
        fovy= fov, 
        aspect= aspect_ratio, 
        near= nearZ, 
        far= farZ
        )
        prog['u_projection'].value = tuple(self.perspective.flatten())
        
    def Teleport(self,x: float,y: float,z: float) -> pyrr.matrix44:
        """Teleports the camera to a coordinate"""
        self.translation = pyrr.matrix44.create_from_translation(pyrr.Vector3([x, y, z])) 
        self.GetViewMatrix()
        
    def Rotation(self, pitch: float, yaw: float, roll:float) -> pyrr.matrix44:
        """Sets rotation for the camera"""
        self.rotation = pyrr.matrix44.create_from_x_rotation(pitch) @ pyrr.matrix44.create_from_y_rotation(yaw) @ pyrr.matrix44.create_from_z_rotation(roll)
        self.forwardvec = self.rotation[2][:3] # If you want to use the forward vector, its available
        self.GetViewMatrix()
        
    def GetViewMatrix(self): # To be used in the rendering buffer and passed to GLSL
        ComposedMatrix =  self.rotation @ self.translation
        ViewMatrix = np.linalg.inv(ComposedMatrix)
        prog['u_viewMatrix'].value = tuple(ViewMatrix.flatten())

class Object2D:
    def __init__(self):
        tx,ty = 0.0, 0.0
        
        angle = 0.0
        
        scaleX, scaleY = 1.0, 1.0

        self.translate = np.array([
            [1,  0,  0, 0],
            [0,  1,  0, 0],
            [0,  0,  1, 0],
            [tx, ty, 0, 1]
        ])       
        
        self.rotation  = np.array([
            [ np.cos(angle), np.sin(angle),  0,        0],
            [-np.sin(angle), np.cos(angle),  0,        0],
            [      0,              0,        1,        0],
            [      0,              0,        0,        1]
        ])    
        
        self.scale = np.array([
            [scaleX,    0,     0,   0],
            [  0,     scaleY,  0,   0],
            [  0,       0,     1,   0],
            [  0,       0,     0,   1]
        ])    
        self.GetMatrix()

    def Teleport(self,tx: float,ty: float):
        self.translate = np.array([
            [1,  0,  0, 0],
            [0,  1,  0, 0],
            [0,  0,  1, 0],
            [tx, ty, 0, 1]
        ])    
        self.GetMatrix()
    def Rotation(self,angle: float):
        self.rotation  = np.array([
            [ np.cos(angle), np.sin(angle),  0,        0],
            [-np.sin(angle), np.cos(angle),  0,        0],
            [      0,              0,        1,        0],
            [      0,              0,        0,        1]
        ])  
        self.GetMatrix()
        
    def Scale(self, xSize: float, ySize:float):
        self.scale = np.array([
            [xSize,     0,     0,   0],
            [  0,      ySize,  0,   0],
            [  0,       0,     1,   0],
            [  0,       0,     0,   1]
        ]) 
        
    def GetMatrix(self):
        Matrix =  self.rotation @ self.translate @ self.scale
        prog_2D['u_translate'] = tuple(Matrix.flatten())
        
    
class Object3D:
    def __init__(self):
        self.translation = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0]))
        self.rotation = pyrr.matrix44.create_from_z_rotation(0) @ pyrr.matrix44.create_from_y_rotation(0) @ pyrr.matrix44.create_from_x_rotation(0)
        self.scale = pyrr.matrix44.create_from_scale(pyrr.Vector3([1.0, 1.0, 1.0]))
        self.GetMatrix()
           
    def Teleport(self,x: float, y:float, z: float) -> pyrr.matrix44:
        """Teleports the object to a coordinate"""
        self.translation = pyrr.matrix44.create_from_translation(pyrr.Vector3([x, y, z]))
        self.GetMatrix()
        
    def Rotate(self, pitch: float, yaw: float, roll: float) -> pyrr.matrix44:
        """Sets rotation for the object"""
        self.rotation = pyrr.matrix44.create_from_x_rotation(pitch) @ pyrr.matrix44.create_from_y_rotation(yaw) @ pyrr.matrix44.create_from_z_rotation(roll)
        self.GetMatrix()
    
    def Scale(self, x: float, y:float, z:float):
        """Sets scale for the object"""
        self.scale = pyrr.matrix44.create_from_scale(pyrr.Vector3([x, y, z]))
        self.GetMatrix()
        
        
    def GetMatrix(self):
        Matrix =   self.rotation @ self.translation @ self.scale
        prog['u_transform'].value = tuple(Matrix.flatten())
        
def BaseColor(nRed: float, nGreen: float, nBlue: float):
    """ Color for the objects. Send inputs *Normalized* \n 
    example: R: 255 -> R: 1.0
    """
    prog['u_color'].value = [nRed, nGreen, nBlue]
        
def Load3DModel(modelName: str, isEdge: bool):
    """Loads a 3D bin model to be used in a buffer,
    list contains [vertices,faceNormals]
    """
    
    with open(f"{current_dir}/{modelName}.bin","rb") as f:
        vertices = f.read()
        
    vboVertices = ctx.buffer(vertices)
        
    if isEdge:
        
        vao = ctx.vertex_array(prog, [(vboVertices, '3f', 'in_vert')])
        
        
    
    else:
        with open(f"{current_dir}/{modelName}_normals.bin","rb") as f:
            vertices_normal = f.read()
            
        vboNormal = ctx.buffer(vertices_normal)
            
        vao = ctx.vertex_array(
            prog,
            [
                (vboVertices, '3f', 'in_vert'),
                (vboNormal, '3f', 'in_normal'),
            ]
        )    

        
    return vao

def LetterConsole(Character: str)-> list[float]:
    CoordsXList = None
    YvalueHeight = None
    numbersNstuff = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
                     ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                     ['1','2','3','4','5','6','7','8','9','0'],
                     ['.', ':', ',' ,';' ,"'" ,'"' ,'(' ,'!' ,'?' ,')' ,'+' ,'-' ,'*' ,'/' ,'=']
                     ]
    #ultimo numero nas listas UVcoords sao a altura de cada um 
    UVcoords = [
        [0.0383, 0.0729, 0.108, 0.1402, 0.1747, 0.205, 0.235, 0.2702, 0.3, 0.3225, 0.3524, 0.383, 0.4172, 0.457, 0.4916, 0.527, 0.5614, 0.5955, 0.623, 0.654, 0.6844, 0.719, 0.7554, 0.795, 0.8297, 0.8627, -0.62], #lwc
        [0.0401, 0.0771, 0.1162, 0.1535, 0.1909, 0.2251, 0.2618, 0.3008, 0.3355, 0.3642, 0.3981, 0.4343, 0.4699, 0.5118, 0.5504, 0.5889, 0.6259, 0.666, 0.7022, 0.7381, 0.7742, 0.8135, 0.8557, 0.8979, 0.9342, 0.97, -0.94],  #hwc
        [0.0383, 0.0745, 0.1104, 0.1444, 0.1798, 0.2141, 0.2498, 0.2819, 0.3131, 0.3473, 0.74], #numb 
        [0.383, 0.412, 0.443, 0.4663, 0.4897, 0.5153, 0.5436, 0.5719, 0.602, 0.6339, 0.6683, 0.7046, 0.7361, 0.7686, 0.8053, 0.74], #specialChar 
        
    ]
    # ordenados na ordem do NumberNstuff

    if Character == ' ':
        CoordsXList = 0.0
        YvalueHeight = 0.0
    elif Character.islower():
        for index, strings in enumerate(numbersNstuff[0]):
            if Character == strings:
                CoordsXList = UVcoords[0][index]
                YvalueHeight = UVcoords[0][len(UVcoords[0]) - 1]
    elif Character.isupper():
        for index, strings in enumerate(numbersNstuff[1]):
            if Character == strings:
                CoordsXList = UVcoords[1][index]
                YvalueHeight = UVcoords[1][len(UVcoords[1]) - 1]
    elif Character.isnumeric():
        for index, strings in enumerate(numbersNstuff[2]):
            if Character == strings:
                CoordsXList = UVcoords[2][index]
                YvalueHeight = UVcoords[2][len(UVcoords[2]) -1]
    else:
        for index, strings in enumerate(numbersNstuff[3]):
            if Character == strings:
                CoordsXList = UVcoords[3][index]
                YvalueHeight = UVcoords[3][len(UVcoords[3]) -1]
                
    return [CoordsXList,YvalueHeight]
            
def SendTextToRender(Text:str, Parent: float):
    positionLetter = 0
    gabeNewline = 0
    for index, charachter in enumerate(Text):

    
        if charachter == "\n":
            gabeNewline += 1
            positionLetter = 0
            continue
        Font.Teleport(-0.9 + positionLetter * 0.03, (-0.23 - 0.085* gabeNewline) - Parent)
        positionLetter += 1
        
        prog_2D['u_texture'] = 0
        prog_2D['u_uv'] = [1, 3.5]
        prog_2D['uv_offset'] = LetterConsole(charachter)
        FONT_vao.render(moderngl.TRIANGLES)
        

    
    


#===========================================================================================================================



        
        


RESOLUCAO = (1280,800)

BG_R = 0.01
BG_G = 0.01
BG_B = 0.01
# cores do background

pygame.init()

pygame.display.set_mode(RESOLUCAO, pygame.DOUBLEBUF | pygame.OPENGL)

ctx = moderngl.create_context()
inmagem = Image.open(f"{current_dir}/terminal_jogo.png").convert()  
SysFont = Image.open(f"{current_dir}/SysLetters.png").convert()  
cursor_source = Image.open(f"{current_dir}/cursor.png").convert()  

Terminal = ctx.texture((1280,387), components=4, data=inmagem.tobytes())
FontSys = ctx.texture((880,120), components=4, data=SysFont.tobytes())
Cursor = ctx.texture((18,30),components=4, data=cursor_source.tobytes())


#=============================================================
# Vertex e frag shader

with open(f"{current_dir}/shaders/vertex.vert","r") as shaderVert:
    vertex_shader = shaderVert.read()
    
with open(f"{current_dir}/shaders/fragment.frag","r") as shaderFrag:
    fragment_shader = shaderFrag.read()
    
with open(f"{current_dir}/shaders/vertex2D.vert","r") as shaderVert:
    vertex_shader2D = shaderVert.read()
    
with open(f"{current_dir}/shaders/fragment2D.frag","r") as shaderFrag:
    fragment_shader2D = shaderFrag.read()


# ===========================================================

prog = ctx.program(
    vertex_shader= vertex_shader,
    fragment_shader= fragment_shader
)

prog_2D = ctx.program(
    vertex_shader= vertex_shader2D,
    fragment_shader= fragment_shader2D
)

# ===========================================================
# parte 2d

Layer2D = np.array([    
    -1, -1,   1, -1,   -1,  -0.15,
     1, -1,   1,  -0.15,   -1,  -0.15,
], dtype='f4')

Layer2Dtwo = np.array([    
    -0.045, -0.035,   -0.045, 0.037,   -0.012, -0.035,
    -0.045, 0.037 ,   -0.012, 0.037,   -0.012, -0.035,

], dtype='f4')

Terminal_vbo = ctx.buffer(Layer2D)
Terminal_vao = ctx.simple_vertex_array(prog_2D, Terminal_vbo, 'in_vert')

FONT_vbo = ctx.buffer(Layer2Dtwo)
FONT_vao = ctx.simple_vertex_array(prog_2D, FONT_vbo, 'in_vert')

# ===========================================================

vao = Load3DModel(modelName= "ship",isEdge= False)
edge_vao = Load3DModel(modelName= "shipEdges",isEdge= True)

Warship = Load3DModel(modelName="warship",isEdge= False)

litteship = Load3DModel(modelName="litteship", isEdge= False)

cruzadeiro = Load3DModel(modelName="cruzadeiro", isEdge= False)

board = Load3DModel(modelName="Boardframe",isEdge= True)

INIMIGOboard = Load3DModel(modelName="BoardframeINIMIGO",isEdge= True)




# ===========================================================

CameraViewer = Camera3D()

PortaAvioes = Object3D()

Console = Object2D()

Font = Object2D()

Board = Object3D()
ctx.clear(BG_R, BG_G, BG_B, 1.0, 1.0)

#=================================================================


Terminal.use(1)
FontSys.use(0)

ctx.enable(moderngl.DEPTH_TEST)


ctx.screen.use()

#.....................................
# Logica do jogo em si

UP = True
DOWN = False
XAXIS = 0
YAXIS = 1
# sinceramente nem sei mas o q estou fazendo


Position = DOWN
RequestMudanca = False
ctx.line_width = 3.0

Console.Teleport(0, -1.0)
CameraViewer.Teleport(0.0, 0.0, 0.0)
yPos = -1.0
CameraTranslate = 5.0
CameraVectorROT = [0.0, 0.0] # O z nao vai mudar 
SendInput = True

GameText = """Bem vindo capitao nome ao sistemas Radar do submarino divisao 5Xyz
Qual o comando que deseja fazer?
Comando: """
Pendingpramandar = ""

while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Position = not Position #ficou feio mas eu tentei fazer com o XOR e n funcionou
                RequestMudanca = True
            if event.key == pygame.K_0:
                Pendingpramandar += "0"
                GameText += "0"
            if event.key == pygame.K_1:
                Pendingpramandar += "1"
                GameText += "1"
            if event.key == pygame.K_2:
                Pendingpramandar += "2"
                GameText += "2"
            if event.key == pygame.K_3:
                Pendingpramandar += "3"
                GameText += "3"
            if event.key == pygame.K_4:
                Pendingpramandar += "4"
                GameText += "4"
            if event.key == pygame.K_5:
                Pendingpramandar += "5"
                GameText += "5"
            if event.key == pygame.K_6:
                Pendingpramandar += "6"
                GameText += "6"
            if event.key == pygame.K_7:
                Pendingpramandar += "7"
                GameText += "7"
            if event.key == pygame.K_8:
                Pendingpramandar += "8"
                GameText += "8"
            if event.key == pygame.K_9:
                Pendingpramandar += "9"
                GameText += "9"
                
                
        if event.type == pygame.MOUSEWHEEL and Position == DOWN:
             CameraTranslate -= 0.5 * event.y # pra cima event.y = 1 pra baixo event.y = -1
        elif event.type == pygame.MOUSEWHEEL:
            i+= 1 * event.y


    teclas = pygame.key.get_pressed()
    #.........................................................................................................................
    # camera rotação
    if teclas[pygame.K_a] and Position == DOWN:
        CameraVectorROT[YAXIS] -= 0.01 # eu amo IMPRECISÃO DE FLOAT por isso faço todos meus calculos usando eles!!! 


    if teclas[pygame.K_d] and Position == DOWN:
        CameraVectorROT[YAXIS] += 0.01 


    if teclas[pygame.K_w] and Position == DOWN:
        CameraVectorROT[XAXIS] -= 0.01 


    if teclas[pygame.K_s] and Position == DOWN:
        CameraVectorROT[XAXIS] += 0.01 



    CameraViewer.Rotation(CameraVectorROT[XAXIS],CameraVectorROT[YAXIS],0.0)
    CameraViewer.Teleport((CameraViewer.forwardvec[0] * CameraTranslate), #xyz
                          (CameraViewer.forwardvec[1] * CameraTranslate), 
                          (CameraViewer.forwardvec[2] * CameraTranslate)) 
    #........................................................................................................................ 

    if RequestMudanca:
    
        if Position == UP and yPos < 0.0:
            yPos += 0.05
        #   Console.Teleport(0, -(yPos ** 2))
        elif Position == UP and yPos >= 0.0:
            RequestMudanca = False
        #.....................................
        if Position == DOWN and yPos > -1.0:
            yPos -= 0.05
        #    Console.Teleport(0, -(yPos ** 2))
        elif Position == DOWN and yPos <= -1.0:
            RequestMudanca = False

    

            
            
            
    #====================================
    ctx.clear(BG_R, BG_G, BG_B)
    
    SendTextToRender(GameText,(np.square(yPos)))
    
    
    Console.Teleport(0, -np.square(yPos))
    prog_2D['u_texture'] = 1
    prog_2D['u_uv'] = [0.5, 1.177]
    prog_2D['uv_offset'] = [0.0, 0.0]
    Terminal_vao.render(moderngl.TRIANGLES)
    

    #....................................
    PortaAvioes.Teleport(0.0,  0.0, 0.0)
    PortaAvioes.Rotate(0.0, 0.0, 0.0) 
    #....................................
    BaseColor(0.0, 1.0, 0.0)
    vao.render(moderngl.TRIANGLES)
    BaseColor(0.0, 1.0, 0.0)
    Board.Teleport(0.0, 0.0, 0.0)
    board.render(moderngl.LINES)
    BaseColor(1.0, 0.0, 0.0)
    INIMIGOboard.render(moderngl.LINES)
    #....................................
    BaseColor(0.0, 0.0, 0.0)
    edge_vao.render(moderngl.LINES)
    
    #....................................


    pygame.display.flip()
    pygame.time.wait(10)