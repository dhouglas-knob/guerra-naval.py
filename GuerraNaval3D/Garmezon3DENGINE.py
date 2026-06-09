import pyrr
import numpy as np

# Define camera class. Since  i plan on making this for a game where the player has minimal control of the camera i won't implement
# the necessary features for free camera mode such as calculating forward and right vectors

class Camera3D:
    def __init__(self):
        self.translation = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0])) 
        self.rotation = pyrr.matrix44.create_from_x_rotation(0) @ pyrr.matrix44.create_from_y_rotation(0) @ pyrr.matrix44.create_from_z_rotation(0)
        self.perspective = pyrr.matrix44.create_perspective_projection_matrix(
        fovy= 90, 
        aspect= 1, 
        near= 1, 
        far= 1000
        )
        # Sets the default values so that the camera can exist before you send any inputs to it
        
    def CameraPerspective(self, fov: int,aspect_ratio: int, nearZ:float,farZ:float) -> pyrr.matrix44:
        """Sets the camera perspective"""
        self.perspective = pyrr.matrix44.create_perspective_projection_matrix(
        fovy= fov, 
        aspect= aspect_ratio, 
        near= nearZ, 
        far= farZ
        )
    def Teleport(self,x: float,y: float,z: float) -> pyrr.matrix44:
        """Teleports the camera to a coordinate"""
        self.translation = pyrr.matrix44.create_from_translation(pyrr.Vector3([x, y, z])) 
        
    def Rotation(self, pitch: float, yaw: float, roll:float) -> pyrr.matrix44:
        """Sets rotation for the camera"""
        self.rotation = pyrr.matrix44.create_from_x_rotation(pitch) @ pyrr.matrix44.create_from_y_rotation(yaw) @ pyrr.matrix44.create_from_z_rotation(roll)
        # Roll gets applied first, then yaw, then pitch.  
        
    def GetViewMatrix(self): # To be used in the rendering buffer and passed to GLSL
        ComposedMatrix =  self.rotation @ self.translation 
        ViewMatrix = np.linalg.inv(ComposedMatrix)
        return ViewMatrix
        
    
class Object3D:
    def __init__(self):
        self.translation = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0]))
        self.rotation = pyrr.matrix44.create_from_z_rotation(0) @ pyrr.matrix44.create_from_y_rotation(0) @ pyrr.matrix44.create_from_x_rotation(0)
        self.scale = pyrr.matrix44.create_from_scale(pyrr.Vector3([1.0, 1.0, 1.0]))
           
    def Teleport(self,x: float, y:float, z: float) -> pyrr.matrix44:
        """Teleports the object to a coordinate"""
        self.translation = pyrr.matrix44.create_from_translation(pyrr.Vector3([x, y, z]))
        
    def Rotate(self, pitch: float, yaw: float, roll: float) -> pyrr.matrix44:
        """Sets rotation for the object"""
        self.rotation = pyrr.matrix44.create_from_x_rotation(pitch) @ pyrr.matrix44.create_from_y_rotation(yaw) @ pyrr.matrix44.create_from_z_rotation(roll)

    
    def Scale(self, x: float, y:float, z:float):
        """Sets scale for the object"""
        self.scale = pyrr.matrix44.create_from_scale(pyrr.Vector3([1.0, 1.0, 1.0]))
        
    def GetMatrix(self):
        Matrix = self.rotation @ self.translation @ self.scale
        return Matrix
        