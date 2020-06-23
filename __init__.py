bl_info = {
    "name": "BMOI Connector",
    "author": "Titus Lavrov / Email: Titus.mailbox@gmail.com",
    "version": (0, 1, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Toolbar and View3D",
    "warning": "",
    "description": "Bridge between MOI and Blender",
    "wiki_url": ""
                "",
    "category": "Import-Export",
}

import bpy
import os
import os.path
import tempfile
from bpy.types import (
        Operator,
        Menu,
        Panel,
        PropertyGroup,
        AddonPreferences,
        )
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        PointerProperty,
        StringProperty,
        )
#Functions

def BMOI_Export(): 
    
    #---Variables---
    customPath = bpy.context.preferences.addons['BMOI_Connector'].preferences.tempFolder
    if customPath == '':            
        path = "" + tempfile.gettempdir() + "\\BMOI"
        path = '/'.join(path.split('\\'))
        if not os.path.exists(path):
            os.makedirs(path)
    else:
        path = bpy.context.preferences.addons['BMOI_Connector'].preferences.tempFolder
    
    temp_file_moi = path + "/BMOI_TMP_MOI.fbx"
    temp_file_blender = path + "/BMOI_TMP_BLENDER.obj"       
              
    #---EXPORT---
    export_scale = bpy.context.preferences.addons['BMOI_Connector'].preferences.export_scale
    # bpy.ops.export_scene.fbx(filepath = temp_file_blender,
    #                              check_existing=True,
    #                              filter_glob="*.fbx",                                  
    #                              use_selection=True, 
    #                              use_active_collection=False, 
    #                              global_scale=global_scale, 
    #                              apply_unit_scale=True, 
    #                              apply_scale_options='FBX_SCALE_ALL', 
    #                              bake_space_transform=True, 
    #                              object_types={'MESH'}, 
    #                              use_mesh_modifiers=True, 
    #                              use_mesh_modifiers_render=True, 
    #                              mesh_smooth_type='OFF', 
    #                              use_mesh_edges=False, 
    #                              use_tspace=False, 
    #                              use_custom_props=False, 
    #                              add_leaf_bones=False, 
    #                              primary_bone_axis='Y', 
    #                              secondary_bone_axis='X', 
    #                              use_armature_deform_only=False, 
    #                              armature_nodetype='NULL', 
    #                              bake_anim=False, 
    #                              bake_anim_use_all_bones=False, 
    #                              bake_anim_use_nla_strips=False, 
    #                              bake_anim_use_all_actions=False, 
    #                              bake_anim_force_startend_keying=False, 
    #                              bake_anim_step=1, 
    #                              bake_anim_simplify_factor=1, 
    #                              path_mode='AUTO', 
    #                              embed_textures=False, 
    #                              batch_mode='OFF', 
    #                              use_batch_own_dir=True, 
    #                              use_metadata=True, 
    #                              axis_forward='Y', 
    #                              axis_up='Z'
    #                             )    
     # ---EXPORT---
    bpy.ops.export_scene.obj(filepath=temp_file_blender,
                             check_existing=True,
                             axis_forward='-Z',
                             axis_up='Y',
                             filter_glob="*.obj;*.mtl",
                             use_selection=True,
                             use_animation=False,
                             use_mesh_modifiers=False,
                             # use_mesh_modifiers_render = False,
                             use_edges=False,
                             use_smooth_groups=False,
                             use_smooth_groups_bitflags=False,
                             use_normals=True,
                             use_uvs=True,
                             use_materials=True,
                             use_triangles=False,
                             use_nurbs=False,
                             use_vertex_groups=False,
                             use_blen_objects=False,
                             group_by_object=True,
                             group_by_material=False,
                             keep_vertex_order=True,
                             global_scale=export_scale,
                             path_mode='AUTO')
   
                

def BMAX_Import():    
    #---Variables---         
    customPath = bpy.context.preferences.addons['BMOI_Connector'].preferences.tempFolder
    if customPath == '':            
        path = "" + tempfile.gettempdir() + "\\BMOI"
        path = '/'.join(path.split('\\'))
        if not os.path.exists(path):
            os.makedirs(path)
    else:
        path = bpy.context.preferences.addons['BMOI_Connector'].preferences.tempFolder
    
    temp_file_moi = path + "/BMOI_TMP_MOI3D.fbx"
    temp_file_blender = path + "/BMOI_TMP_BLENDER.fbx"            
       
    #---IMPORT---        
    #---Import FXB---
    import_scale = bpy.context.preferences.addons['BMOI_Connector'].preferences.import_scale
    if os.path.isfile(temp_file_moi) == True: 
        bpy.ops.import_scene.fbx(filepath=temp_file_moi, 
                                         directory="", 
                                         filter_glob="*.fbx",
                                         use_manual_orientation=False, 
                                         global_scale=import_scale, 
                                         bake_space_transform=False, 
                                         use_custom_normals=True, 
                                         use_image_search=False, 
                                         use_alpha_decals=False, 
                                         decal_offset=0, 
                                         use_anim=False, 
                                         anim_offset=1, 
                                         use_custom_props=False, 
                                         use_custom_props_enum_as_string=False, 
                                         ignore_leaf_bones=False, 
                                         force_connect_children=False, 
                                         automatic_bone_orientation=False, 
                                         primary_bone_axis='Y', 
                                         secondary_bone_axis='X', 
                                         use_prepost_rot=True, 
                                         axis_forward='-Z', 
                                         axis_up='Y'
                                         )
        if len(bpy.context.selected_objects) != 0:            
            bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True) 

class BMOI3D_OT_Export(Operator):
    bl_idname = "bmoi3d.export"
    bl_label = "Send to MOI3D"
    bl_description = "Export model to MoI3D"
    bl_options = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):        
        if len(bpy.context.selected_objects) == 0:
            self.report ({'INFO'}, 'Selection is empty! Please select some objects!!') 
            return {'FINISHED'}
        else:
            BMOI_Export()
            self.report ({'INFO'}, 'BMOI3D - EXPORT DONE!')
            return {'FINISHED'}

class BMOI3D_OT_Import(Operator):
    bl_idname = "bmoi3d.import"
    bl_label = "Import from MOI3D"
    bl_description = "Import model from MoI3D"
    bl_options = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):        
        BMAX_Import()
        self.report ({'INFO'}, 'BMAX - IMPORT DONE!')
        return {'FINISHED'}
        
# panel containing all tools
class VIEW3D_PT_BMOI3D(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BMOI3D'    
    bl_label = "BMOI3D Conector"
    
    def draw(self, context):
        prefs = bpy.context.preferences.addons['BMOI_Connector'].preferences
        layout = self.layout       
        
        col = layout.column(align=True)
        col.prop(prefs,"export_scale")
        col.prop(prefs,"import_scale")
        col.scale_y = 1.5
        col.operator('bmoi3d.export', icon='EXPORT',text = "Send to MOI3D")
        col.operator('bmoi3d.import',icon='IMPORT', text="Get from MOI3D")
        
class BMOI3D_AddonPreferences(AddonPreferences):
    bl_idname = __name__    

    export_scale: FloatProperty(
        name="Export Scale",
        description="Export Global Scale",
        default=100,
        min=0.000,
        max=1000000000.000,
        step=0.1,
        precision=3
    )

    import_scale: FloatProperty(
        name="Import Scale",
        description="Import Global Scale",
        default=1,
        min=0.000,
        max=1000000000.000,
        step=0.1,
        precision=3
    )


    tempFolder : StringProperty(
        name = "BMOI3D custom exchange folder",
        subtype = 'DIR_PATH',
        )  

    def draw(self, context):        
        props = bpy.context.preferences.addons[__name__].preferences    
        
        layout = self.layout
        col = layout.column(align=True)
        col.label(text = "FBX import/export global scale")
        col.prop(self, "export_scale")
        col.prop(self, "import_scale")               
        col.label(text = "Select custom BMOI3D exchange folder(keep it empty for default BMAX folder)")
        col.prop(self, "tempFolder") 

 
#Classes for register and unregister
classes = (
            BMOI3D_OT_Export,
            BMOI3D_OT_Import,
            VIEW3D_PT_BMOI3D,             
            BMOI3D_AddonPreferences         
        )
    
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    print ("BMOI3D Connector - Registred!")

def unregister(): 
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    print ("BMOI3D Connector - UnRegistred!")

if __name__ == "__main__":
    register()