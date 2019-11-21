import bpy
import bmesh

bl_info = {
 "name": "Vertices Position Rounder",
 "author": "1nZ4N3",
 "version": (1, 0, 0),
 "blender": (2, 80, 0),
 "location": "3D View",
 "description": "To help round the vertices position in to 2 decimals",
 "warning": "",
 "wiki_url": "",
 "tracker_url": "",
 "category": "Object"}

class Rounder(bpy.types.Operator):  
    
    bl_label = "Round vertices position"
    bl_idname = "object.rounder"
    bl_options = {'REGISTER', 'UNDO'}
    
    def Rounding(self):
        # Get the selected objects
        objs = bpy.context.selected_objects
        
        for obj in objs:
            me = obj.data
            # Get a BMesh representation
            bm = bmesh.new()   # create an empty BMesh
            bm.from_mesh(me)   # fill it in from a Mesh


            # Round vertices position in local space
            for vert in bm.verts:
                vert.co.x = round(vert.co.x, 2)
                vert.co.y = round(vert.co.y, 2)
                vert.co.z = round(vert.co.z, 2)

            # Finish up, write the bmesh back to the mesh
            bm.to_mesh(me)
            bm.free()  # free and prevent further access
            me.update() # Update mesh
    
    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT' and context.area.type == 'VIEW_3D'
        
    def execute(self, context):
        self.Rounding()
        return {'FINISHED'}

class RounderPanel(bpy.types.Panel):
    
    bl_idname = "OBJECT_PT_tools"
    bl_label = "Vertices Position Rounder Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "objectmode"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        
        layout = self.layout
        
        col = layout.column(align=True)
        col.operator("object.rounder")
        
    
#registers    
    
def register():
    bpy.utils.register_class(Rounder)
    bpy.utils.register_class(RounderPanel)

def unregister():
    bpy.utils.unregister_class(Rounder)
    bpy.utils.unregister_class(RounderPanel)

if __name__ == "__main__":
    register()
