
// ------------------------ Rocket 3F/MoI Bridge 1.3------------------------

var Bmoi_path = "c:/Users/Titus/AppData/Local/Temp/BMOI/BMOI_TMP_MOI3D.fbx"	
	

function Export_to_Blender()
{ 	
	var so = moi.geometryDatabase.getSelectedObjects(); 
	if ( so.length == 0 ) 
	{
		moi.ui.alert("Nothing is selected.");
	}
	else
	{
		bmoi_export_FBX()
		
		function bmoi_export_FBX()
		{
			moi.geometryDatabase.fileExport(Bmoi_path, 'NoUI=False');			
		}
	}
	
}

Export_to_Blender()
	
	
	