// ImportObj v.1.5 - Max Smirnov. 2015 + Modified version by Titus (Titus.mailbox@gmail.com)
function getMethods(obj) {
	var result = [];
	for (var id in obj) {
	  try {
		if (typeof(obj[id]) == "function") {
		  result.push(id + ": " + obj[id].toString());
		}
	  } catch (err) {
		result.push(id + ": inaccessible");
	  }
	}
	return result;
  }

function importObj()
{
	var MoI_dir = moi.filesystem.getAppDataDir();
	var Base_dir = MoI_dir.substr( 0, MoI_dir.length - 13 );
	var first_letter = MoI_dir.substr( 0, 2 );
	var is_mac = first_letter == "z:" ? true : false;

	var objPath = Base_dir + '\\Local\\Temp\\BMOI\\BMOI_TMP_BLENDER.obj'
	if(is_mac){
		objPath = MoI_dir + '\\BMOI\\BMOI_TMP_BLENDER.obj'
	}	

	if ( !objPath ) return false;
	moi.ui.commandUI.progressinfo.innerHTML="Loading"; 
	moi.ui.commandUI.loadObj( objPath );
	var facesnum = moi.ui.commandUI.faces.length;
	moi.ui.commandUI.progressinfo.innerHTML="Normalizing"; 
	if ( moi.command.getCommandLineParams() ==='exact' ) { moi.ui.commandUI.normalizeObj( false ) } else { moi.ui.commandUI.normalizeObj( true ) }
	var cstart = 0, cend=0, cstep = 2000;
	do {	cend = (cend+cstep>facesnum)?facesnum:cend+cstep;
		moi.ui.commandUI.progressinfo.innerHTML="Processing ("+cstart+"/"+facesnum+")<br/>Press ESC to abort"; 
		moi.ui.commandUI.processObj(cstart, cend); 
		cstart +=cstep;
	} while (cend<facesnum);
	moi.ui.commandUI.progressinfo.innerHTML="Resizing"; 
	moi.ui.commandUI.showObj();
	moi.ui.commandUI.progressinfo.innerHTML="Joining<br/>Press ESC to skip"; 
	moi.ui.commandUI.joinObj(20000);
	moi.ui.commandUI.progressinfo.innerHTML=""; 
}
importObj();