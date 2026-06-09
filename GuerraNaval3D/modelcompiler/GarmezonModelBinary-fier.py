import os 
import struct
import numpy as np
import math
import sys
current_dir = os.getcwd()



MODEL = current_dir + "/modelcompiler/BoardframeINIMIGO.obj"

NOME = "BoardframeINIMIGO"

AreEdges = True

# ========================= #

vertices = []

vertices_normals = []

faces_information = []

vertices_processed = []

vertices_normals_processed = []

faces_processed = []     

face_normals = []
face_normalsWrite = []

VerticesWriteFile = []

VerticesNormalsWriteFile = []

lines = []

lines_processed = []


# ========================= #

# Not grabbing the UV texture coordinate since we're not using textures in the fragment shader
# Não estou pegando as coordenadas de textura UV já que não estamos usando texturas na fragment shader


with open(MODEL,'r') as file:
    for line in file:
        if line.startswith("v "):
            vertex = line.replace("v ","").strip().split(" ")
            vertices.append([float(i) for i in vertex])
        if line.startswith("l "):
            lineEdge = line.replace("l ","").strip().split(" ")
            lines.append([float(i) for i in lineEdge])
        if line.startswith("vn"):
            vertex_normal = line.replace("vn","").strip().split(" ")
            vertices_normals.extend([float(i) for i in vertex_normal])
        if line.startswith("f"):
            faceInfo = line.replace("f","").strip().split(" ")
            faces_information.append(faceInfo)
            
            
            
# f contains indexes that point to specific v and vn (and vt, but we're not using that)
# f contém indíces que apontam para um v e vn especifico ( e vt, mas não estamos usando esse)
if not AreEdges:
    for vertex_indexes in faces_information:
        for indexes in vertex_indexes:
            index = indexes.split("/")
            faces_processed.append([int(i) for i in index])

    for lists in faces_processed:
        vertices_processed.append(vertices[lists[0] - 1])
        
            
    print(len(vertices_processed))

    for lists in vertices_processed:
        for indices in lists:
            VerticesWriteFile.append(indices)
        
    with open(current_dir + f"/{NOME}.bin","wb") as Newfile:
        PackedVertices = struct.pack(f'{len(VerticesWriteFile)}f', *VerticesWriteFile)
        Newfile.write(PackedVertices)
        
    for lists in faces_processed:
        vertices_normals_processed.append(vertices[lists[2] - 1])
        
        
    for lists in vertices_normals_processed:
        for indices in lists:
            VerticesNormalsWriteFile.append(indices)
            
    print(len(vertices_processed))
            
    for i in range(0, len(vertices_processed), 3):


        a = np.array(vertices_processed[i])
        b = np.array(vertices_processed[i+1])
        c = np.array(vertices_processed[i+2])
        
        uVec = a - b
        vVec = a - c
        
        VectorCross = np.cross(uVec,vVec)
        
        Normalize = np.linalg.norm(VectorCross)
        
        if Normalize < 1e-10:  # degenerate triangle guard
            print(f"Warning: degenerate triangles, stopping the compile")
            sys.exit()
        
        Normalfinal = VectorCross / Normalize 
        
        face_normals.append(Normalfinal)
        
    for lists in face_normals:
        
        face_normals_processed = []
        for indices in lists:
            face_normals_processed.append(indices)
        face_normalsWrite.extend(face_normals_processed)
        face_normalsWrite.extend(face_normals_processed)
        face_normalsWrite.extend(face_normals_processed)






    print(len(face_normalsWrite),len(VerticesWriteFile))
    print(face_normalsWrite[:3])
    print(VerticesWriteFile[:3])
    

        


    #with open(current_dir + f"/{NOME}_normals.bin","wb") as Newfile:
        #PackedVertices = struct.pack(f'{len(VerticesNormalsWriteFile)}f', *VerticesNormalsWriteFile)
        # Newfile.write(PackedVertices)
        
    with open(current_dir + f"/{NOME}_normals.bin","wb") as Newfile:
        PackedVertices2 = struct.pack(f'{len(face_normalsWrite)}f', *face_normalsWrite)
        Newfile.write(PackedVertices2)
else:
    print(lines[:3])
    
    for vertex_indexes in lines:
        for indexes in vertex_indexes:
            lines_processed.append([int(indexes)])
            
    print(lines_processed[:3])
            
    for lists in lines_processed:
        vertices_processed.append(vertices[lists[0] - 1])
        
    for lists in vertices_processed:
        for indices in lists:
            VerticesWriteFile.append(indices)
        
    with open(current_dir + f"/{NOME}.bin","wb") as Newfile:
        PackedVertices = struct.pack(f'{len(VerticesWriteFile)}f', *VerticesWriteFile)
        Newfile.write(PackedVertices)