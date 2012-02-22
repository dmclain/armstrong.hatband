CKEDITOR.editorConfig = function( config )
{
	config.toolbar = 'MyToolbar';
	config.extraPlugins = 'embedobject';
 
	config.toolbar_MyToolbar =
	[
		{ name: 'clipboard', items : [ 'PasteFromWord' ] },
		{ name: 'styles', items : [ 'Format' ] },
		{ name: 'basicstyles', items : [ 'Bold','Italic','Strike','-','RemoveFormat' ] },
		{ name: 'links', items : [ 'Link','Unlink'] },
		{ name: 'embedobject', items : [ 'EmbedObject'] },
	];
};