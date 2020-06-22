// ImportObj v.1.5 - Max Smirnov. 2015
function importObj()
{
	//var objPath = moi.filesystem.getOpenFileName( 'Import OBJ', ' (*.obj)|*.obj' );
	var objPath = "c:/Users/Titus/AppData/Local/Temp/BMOI/BMOI_TMP_BLENDER.obj"
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