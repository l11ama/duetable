{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 6,
			"revision" : 2,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 34.0, 77.0, 762.0, 570.0 ],
		"bglocked" : 0,
		"openinpresentation" : 1,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"assistshowspatchername" : 0,
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-151",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 763.333315134048462, 929.999977827072144, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-149",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 649.999984502792358, 1038.333308577537537, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-147",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 606.666652202606201, 964.999976992607117, 152.0, 22.0 ],
					"text" : "if $i2 > $i1 then $i1 else $2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-144",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 769.999981641769409, 849.999979734420776, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-141",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 832.051235675811768, 961.666643738746643, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-134",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 968.333309054374695, 961.666643738746643, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-135",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "float" ],
					"patching_rect" : [ 916.666643619537354, 928.333311200141907, 39.0, 22.0 ],
					"text" : "/ 100."
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-133",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 999.99997615814209, 876.666645765304565, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-131",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "float" ],
					"patching_rect" : [ 947.974307775497437, 843.999979615211487, 39.0, 22.0 ],
					"text" : "/ 100."
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-130",
					"maxclass" : "number",
					"minimum" : 0,
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 832.051235675811768, 916.666644811630249, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 628.829252004623413, 409.499991536140442, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-129",
					"maxclass" : "number",
					"minimum" : 0,
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 851.089693188667297, 803.333314180374146, 96.666664361953735, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 628.829252004623413, 361.641841113567352, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"bgcolor" : [ 0.890196078431372, 0.784313725490196, 0.129411764705882, 0.75 ],
					"bordercolor" : [ 0.349019607843137, 0.349019607843137, 0.349019607843137, 0.0 ],
					"fontface" : 0,
					"fontsize" : 16.0,
					"id" : "obj-123",
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 841.051235675811768, 838.333313345909119, 51.666665434837341, 33.333332538604736 ],
					"presentation" : 1,
					"presentation_rect" : [ 562.078941822052002, 404.666658580303192, 43.333332300186157, 31.6666659116745 ],
					"text" : "Max",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"bgcolor" : [ 0.890196078431372, 0.784313725490196, 0.129411764705882, 0.75 ],
					"bordercolor" : [ 0.349019607843137, 0.349019607843137, 0.349019607843137, 0.0 ],
					"fontface" : 0,
					"fontsize" : 16.0,
					"id" : "obj-122",
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 841.051235675811768, 763.333315134048462, 51.666665434837341, 33.333332538604736 ],
					"presentation" : 1,
					"presentation_rect" : [ 562.078941822052002, 356.808508157730103, 43.333332300186157, 31.6666659116745 ],
					"text" : "Min ",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"bgcolor" : [ 0.890196078431372, 0.784313725490196, 0.129411764705882, 1.0 ],
					"bordercolor" : [ 0.349019607843137, 0.349019607843137, 0.349019607843137, 0.0 ],
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-121",
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 809.999980688095093, 701.978694558143616, 208.333328366279602, 22.585366129875183 ],
					"presentation" : 1,
					"presentation_rect" : [ 562.078941822052002, 325.641006231307983, 203.846141695976257, 23.076921701431274 ],
					"text" : "Duration Between Notes (ms)",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-112",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1053.246743202209473, 150.649349212646484, 70.0, 22.0 ],
					"text" : "loadmess 0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-111",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 656.666651010513306, 607.792201995849609, 255.84415340423584, 22.0 ],
					"text" : "/MusicalParameters/Key C#maj"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-109",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 788.410208344459534, 534.851892650127411, 186.0, 22.0 ],
					"text" : "prepend /MusicalParameters/Key"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-107",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1103.896093368530273, 245.454543113708496, 50.0, 22.0 ],
					"text" : "maj"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-105",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 987.012977600097656, 314.641006231307983, 57.0, 22.0 ],
					"text" : "keyname"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-98",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 937.974307775497437, 416.883112907409668, 50.0, 22.0 ],
					"text" : "C#maj"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-96",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 974.025964736938477, 345.45454216003418, 139.0, 22.0 ],
					"text" : "combine keyname mode"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-92",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 974.025964736938477, 283.116880416870117, 50.0, 22.0 ],
					"text" : "C#"
				}

			}
, 			{
				"box" : 				{
					"activebgcolor" : [ 1.0, 0.709803921568627, 0.196078431372549, 1.0 ],
					"fontsize" : 20.0,
					"id" : "obj-90",
					"maxclass" : "live.menu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "float" ],
					"parameter_enable" : 1,
					"parameter_mappable" : 0,
					"patching_rect" : [ 1047.331187307834625, 193.333328723907471, 110.526315689086914, 27.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 1039.71606320142746, 216.666653752326965, 79.220778465270996, 27.0 ],
					"saved_attribute_attributes" : 					{
						"activebgcolor" : 						{
							"expression" : "themecolor.live_lcd_control_fg"
						}
,
						"textcolor" : 						{
							"expression" : "themecolor.live_arranger_grid_tiles"
						}
,
						"valueof" : 						{
							"parameter_enum" : [ "maj", "min" ],
							"parameter_longname" : "live.menu[5]",
							"parameter_mmax" : 1,
							"parameter_modmode" : 0,
							"parameter_shortname" : "live.menu",
							"parameter_type" : 2,
							"parameter_unitstyle" : 9
						}

					}
,
					"textcolor" : [ 0.039216, 0.039216, 0.039216, 1.0 ],
					"varname" : "live.menu[5]"
				}

			}
, 			{
				"box" : 				{
					"activebgcolor" : [ 1.0, 0.709803921568627, 0.196078431372549, 1.0 ],
					"fontsize" : 20.0,
					"id" : "obj-89",
					"maxclass" : "live.menu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "float" ],
					"parameter_enable" : 1,
					"parameter_mappable" : 0,
					"patching_rect" : [ 928.333311200141907, 193.333328723907471, 110.526315689086914, 27.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 967.532458305358887, 216.666653752326965, 57.142856597900391, 27.0 ],
					"saved_attribute_attributes" : 					{
						"activebgcolor" : 						{
							"expression" : "themecolor.live_lcd_control_fg"
						}
,
						"textcolor" : 						{
							"expression" : "themecolor.live_arranger_grid_tiles"
						}
,
						"valueof" : 						{
							"parameter_enum" : [ "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B" ],
							"parameter_longname" : "live.menu[4]",
							"parameter_mmax" : 11,
							"parameter_modmode" : 0,
							"parameter_shortname" : "live.menu",
							"parameter_type" : 2,
							"parameter_unitstyle" : 9
						}

					}
,
					"textcolor" : [ 0.039216, 0.039216, 0.039216, 1.0 ],
					"varname" : "live.menu[4]"
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"bgcolor" : [ 0.890196078431372, 0.674509803921569, 0.129411764705882, 1.0 ],
					"bordercolor" : [ 0.349019607843137, 0.349019607843137, 0.349019607843137, 0.0 ],
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-88",
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 951.666643977165222, 137.913465619087219, 57.692304253578186, 41.025638580322266 ],
					"presentation" : 1,
					"presentation_rect" : [ 967.532458305358887, 183.483173131942749, 148.051946640014648, 23.376623153686523 ],
					"text" : "Key",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"varname" : "Bars[4]"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-87",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 691.666650176048279, 461.202124357223511, 173.0, 23.0 ],
					"text" : "/MusicalParameters/BPM $1"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-86",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 656.666651010513306, 403.33332371711731, 214.0, 23.0 ],
					"presentation_linecount" : 2,
					"text" : "/MusicalParameters/UpperMeter $1"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-84",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 683.717901110649109, 433.833323001861572, 209.0, 23.0 ],
					"presentation_linecount" : 4,
					"text" : "/MusicalParameters/lowermeter $1"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-83",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 333.921049833297729, 346.308508157730103, 63.0, 23.0 ],
					"text" : "/nbars $1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-82",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 371.184206604957581, 283.333326578140259, 70.0, 22.0 ],
					"text" : "loadmess 2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-81",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 860.256360471248627, 354.999991536140442, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 869.999979257583618, 286.666659832000732, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-79",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 856.410208344459534, 277.723402261734009, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 866.666646003723145, 353.333324909210205, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-77",
					"maxclass" : "number",
					"minimum" : 0,
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 318.421049833297729, 283.333326578140259, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 319.884599566459656, 240.677954912185669, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-69",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 850.256360471248627, 277.723402261734009, 70.0, 22.0 ],
					"text" : "loadmess 4"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-66",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 798.717901110649109, 16.078947305679321, 83.0, 22.0 ],
					"text" : "loadmess 120"
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"bgcolor" : [ 0.890196078431372, 0.674509803921569, 0.129411764705882, 1.0 ],
					"bordercolor" : [ 0.349019607843137, 0.349019607843137, 0.349019607843137, 0.0 ],
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-65",
					"linecount" : 2,
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 856.410208344459534, 305.128186941146851, 57.692304253578186, 41.025638580322266 ],
					"presentation" : 1,
					"presentation_rect" : [ 866.666615009307861, 320.5128014087677, 101.298700332641602, 23.376623153686523 ],
					"text" : "Lower Meter",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"varname" : "Bars[3]"
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"bgcolor" : [ 0.890196078431372, 0.674509803921569, 0.129411764705882, 1.0 ],
					"bordercolor" : [ 0.349019607843137, 0.349019607843137, 0.349019607843137, 0.0 ],
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-64",
					"linecount" : 2,
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 860.256360471248627, 230.769217014312744, 57.692304253578186, 41.025638580322266 ],
					"presentation" : 1,
					"presentation_rect" : [ 866.666615009307861, 252.865792870521545, 101.298700332641602, 23.376623153686523 ],
					"text" : "Upper Meter",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"varname" : "Bars[2]"
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"bgcolor" : [ 0.890196078431372, 0.674509803921569, 0.129411764705882, 1.0 ],
					"bordercolor" : [ 0.349019607843137, 0.349019607843137, 0.349019607843137, 0.0 ],
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-63",
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 861.538411676883698, 137.913465619087219, 55.128201842308044, 25.59411883354187 ],
					"presentation" : 1,
					"presentation_rect" : [ 874.358922243118286, 183.333322405815125, 50.0, 23.376623153686523 ],
					"text" : "BPM",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"varname" : "Bars[1]"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-61",
					"maxclass" : "number",
					"minimum" : 1,
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 864.10251259803772, 174.973682165145874, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 874.358922243118286, 216.666653752326965, 50.0, 22.0 ],
					"varname" : "barsnum[1]"
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"fontface" : 1,
					"fontsize" : 20.0,
					"id" : "obj-60",
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 858.974307775497437, 76.923072338104248, 208.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 909.174160838127136, 99.0, 206.410244107246399, 34.615382552146912 ],
					"text" : "Musical Parameters",
					"textcolor" : [ 1.0, 0.843137254901961, 0.090196078431373, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-59",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "bang", "" ],
					"patching_rect" : [ 192.553190112113953, 232.978721737861633, 50.0, 22.0 ],
					"text" : "select 3"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-58",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "bang", "" ],
					"patching_rect" : [ 150.425531268119812, 226.595743060112, 50.0, 22.0 ],
					"text" : "select 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-55",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "bang", "" ],
					"patching_rect" : [ 81.9148930311203, 216.473682165145874, 50.0, 22.0 ],
					"text" : "select 2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-47",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "bang", "" ],
					"patching_rect" : [ 14.893616914749146, 216.473682165145874, 50.0, 22.0 ],
					"text" : "select 0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-41",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 125.531913995742798, 276.723402261734009, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-36",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 10.308510303497314, 257.446806669235229, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-22",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 108.510637521743774, 373.404252648353577, 113.0, 22.0 ],
					"presentation_linecount" : 2,
					"text" : "script hide barsnum"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-20",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ -14.0, 373.404252648353577, 119.0, 22.0 ],
					"presentation_linecount" : 2,
					"text" : "script show barsnum"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-19",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 129.925531268119812, 328.72340190410614, 91.0, 22.0 ],
					"text" : "script hide Bars"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-18",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 10.308510303497314, 346.808508157730103, 97.0, 22.0 ],
					"text" : "script show Bars"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-15",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 73.4148930311203, 461.702124357223511, 67.0, 22.0 ],
					"save" : [ "#N", "thispatcher", ";", "#Q", "end", ";" ],
					"text" : "thispatcher"
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"bgcolor" : [ 0.890196078431372, 0.674509803921569, 0.129411764705882, 1.0 ],
					"bordercolor" : [ 0.349019607843137, 0.349019607843137, 0.349019607843137, 0.0 ],
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-3",
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 267.457633018493652, 244.999994158744812, 182.926833629608154, 23.170732259750366 ],
					"presentation" : 1,
					"presentation_rect" : [ 265.384599566459656, 189.361700773239136, 203.846141695976257, 23.076921701431274 ],
					"text" : "Bars to be generated",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"varname" : "Bars"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-46",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1028.205066919326782, 702.564060688018799, 362.0, 22.0 ],
					"text" : "/Transformators/FixedRangeTransformer/Params/IntervalOffset $1"
				}

			}
, 			{
				"box" : 				{
					"activebgcolor" : [ 1.0, 0.709803921568627, 0.196078431372549, 1.0 ],
					"fontsize" : 25.0,
					"id" : "obj-43",
					"maxclass" : "live.menu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "float" ],
					"parameter_enable" : 1,
					"parameter_mappable" : 0,
					"patching_rect" : [ 1037.179425358772278, 592.333318948745728, 110.526315689086914, 33.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 273.421049833297729, 525.640994310379028, 110.526315689086914, 33.0 ],
					"saved_attribute_attributes" : 					{
						"activebgcolor" : 						{
							"expression" : "themecolor.live_lcd_control_fg"
						}
,
						"textcolor" : 						{
							"expression" : "themecolor.live_arranger_grid_tiles"
						}
,
						"valueof" : 						{
							"parameter_enum" : [ "P", "2m", "2M", "3m", "3M", "4m", "4M", "5", "6m", "6M", "7m", "7M", "8" ],
							"parameter_longname" : "live.menu[3]",
							"parameter_mmax" : 12,
							"parameter_modmode" : 0,
							"parameter_shortname" : "live.menu",
							"parameter_type" : 2,
							"parameter_unitstyle" : 9
						}

					}
,
					"textcolor" : [ 0.039216, 0.039216, 0.039216, 1.0 ],
					"varname" : "live.menu[3]"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-40",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1302.678559005260468, 654.464279472827911, 360.0, 22.0 ],
					"text" : "/Transformators/FixedRangeTransformer/Params/MelodyNotes $1"
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"bgcolor" : [ 0.890196078431372, 0.784313725490196, 0.129411764705882, 0.75 ],
					"bordercolor" : [ 0.349019607843137, 0.349019607843137, 0.349019607843137, 0.0 ],
					"fontface" : 0,
					"fontsize" : 14.0,
					"id" : "obj-38",
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1007.505060344934464, 558.035708963871002, 190.178569614887238, 20.535714089870453 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 258.684207677841187, 464.10253643989563, 140.0, 55.0 ],
					"text" : "Interval Offset (in semitones)",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"bgcolor" : [ 0.890196078431372, 0.784313725490196, 0.129411764705882, 0.75 ],
					"bordercolor" : [ 0.349019607843137, 0.349019607843137, 0.349019607843137, 0.0 ],
					"fontface" : 0,
					"fontsize" : 16.0,
					"id" : "obj-35",
					"linecount" : 2,
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 960.630062758922577, 470.535709798336029, 279.0, 46.153843402862549 ],
					"presentation" : 1,
					"presentation_linecount" : 3,
					"presentation_rect" : [ 265.384599566459656, 357.692286372184753, 159.0, 62.0 ],
					"text" : "Number of melody notes to analyse interval range",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 16.0,
					"id" : "obj-34",
					"maxclass" : "number",
					"minimum" : 1,
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1068.630059480667114, 520.512789487838745, 59.0, 27.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 299.184207677841187, 422.31578516960144, 59.0, 27.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-33",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1329.999968290328979, 603.333318948745728, 54.0, 22.0 ],
					"text" : "s python"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-32",
					"linecount" : 2,
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1299.107130467891693, 527.67856639623642, 150.595743775367737, 36.0 ],
					"text" : "/Transformators/FixedRangeTransformer 0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-26",
					"maxclass" : "toggle",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1206.666637897491455, 433.333323001861572, 24.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 476.050019383430481, 320.5128014087677, 39.743587374687195, 39.743587374687195 ]
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"bgcolor" : [ 0.890196078431372, 0.784313725490196, 0.129411764705882, 1.0 ],
					"bordercolor" : [ 0.349019607843137, 0.349019607843137, 0.349019607843137, 0.0 ],
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-11",
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1006.666642665863037, 428.333323121070862, 182.926833629608154, 23.170732259750366 ],
					"presentation" : 1,
					"presentation_rect" : [ 265.384599566459656, 325.641006231307983, 203.846141695976257, 23.076921701431274 ],
					"text" : "Fixed Range Transformer",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-10",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1291.666635870933533, 458.333322405815125, 242.0, 22.0 ],
					"text" : "/Transformators/FixedRangeTransformer $1"
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"fontface" : 1,
					"fontsize" : 24.0,
					"id" : "obj-8",
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1149.999972581863403, 351.666658282279968, 188.33332884311676, 34.999999165534973 ],
					"presentation" : 1,
					"presentation_rect" : [ 562.078941822052002, 258.333327174186707, 244.0, 34.0 ],
					"text" : "Transformators",
					"textcolor" : [ 1.0, 0.843137254901961, 0.090196078431373, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-74",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 581.578941822052002, 310.026312828063965, 145.0, 23.0 ],
					"text" : "/NumberOfNotesDur $1"
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 20.0,
					"id" : "obj-72",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 589.473678588867188, 207.473682165145874, 65.0, 31.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 784.61533784866333, 193.371783256530762, 65.0, 31.0 ]
				}

			}
, 			{
				"box" : 				{
					"activebgcolor" : [ 1.0, 0.709803921568627, 0.196078431372549, 1.0 ],
					"fontsize" : 20.0,
					"id" : "obj-62",
					"maxclass" : "live.menu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "float" ],
					"parameter_enable" : 1,
					"parameter_mappable" : 0,
					"patching_rect" : [ 589.473678588867188, 172.473682165145874, 248.684208154678345, 27.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 529.487147927284241, 194.871783256530762, 248.684208154678345, 27.0 ],
					"saved_attribute_attributes" : 					{
						"activebgcolor" : 						{
							"expression" : "themecolor.live_lcd_control_fg"
						}
,
						"textcolor" : 						{
							"expression" : "themecolor.live_arranger_grid_tiles"
						}
,
						"valueof" : 						{
							"parameter_enum" : [ "Duration(seconds)", "NumberOfNotes" ],
							"parameter_longname" : "live.menu[2]",
							"parameter_mmax" : 1,
							"parameter_modmode" : 0,
							"parameter_shortname" : "live.menu",
							"parameter_type" : 2,
							"parameter_unitstyle" : 9
						}

					}
,
					"textcolor" : [ 0.039216, 0.039216, 0.039216, 1.0 ],
					"varname" : "live.menu[2]"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-56",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 374.999996423721313, 649.999993801116943, 364.102542400360107, 22.0 ],
					"text" : "/RecordingStrategy 0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-54",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 346.0526282787323, 621.05262565612793, 52.0, 22.0 ],
					"text" : "r python"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-53",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 410.526311874389648, 490.789469003677368, 54.0, 22.0 ],
					"text" : "s python"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-52",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 546.753241539001465, 571.428565979003906, 196.052629709243774, 22.0 ],
					"text" : "/RecordingStrategy 0"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-51",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 483.116878509521484, 428.418689250946045, 138.0, 23.0 ],
					"text" : "/RecordingStrategy $1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-49",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 448.026311278343201, 310.526312828063965, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-50",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 489.473679542541504, 214.473682165145874, 50.0, 22.0 ],
					"text" : "Time"
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"fontface" : 1,
					"fontsize" : 20.0,
					"id" : "obj-39",
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 485.499996185302734, 76.923072338104248, 208.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 276.499997138977051, 99.0, 206.410244107246399, 34.615382552146912 ],
					"text" : "Regenerator Type",
					"textcolor" : [ 1.0, 0.843137254901961, 0.090196078431373, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"activebgcolor" : [ 1.0, 0.709803921568627, 0.196078431372549, 1.0 ],
					"fontsize" : 25.0,
					"id" : "obj-31",
					"maxclass" : "live.menu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "float" ],
					"parameter_enable" : 1,
					"parameter_mappable" : 0,
					"patching_rect" : [ 516.94736385345459, 130.769222974777222, 110.526315689086914, 33.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 533.333301544189453, 139.743581414222717, 110.526315689086914, 33.0 ],
					"saved_attribute_attributes" : 					{
						"activebgcolor" : 						{
							"expression" : "themecolor.live_lcd_control_fg"
						}
,
						"textcolor" : 						{
							"expression" : "themecolor.live_arranger_grid_tiles"
						}
,
						"valueof" : 						{
							"parameter_enum" : [ "Time", "Notes" ],
							"parameter_longname" : "live.menu[1]",
							"parameter_mmax" : 1,
							"parameter_modmode" : 0,
							"parameter_shortname" : "live.menu",
							"parameter_type" : 2,
							"parameter_unitstyle" : 9
						}

					}
,
					"textcolor" : [ 0.039216, 0.039216, 0.039216, 1.0 ],
					"varname" : "live.menu[1]"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-30",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 288.157891988754272, 310.526312828063965, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-27",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 313.157891750335693, 549.99999475479126, 196.052629709243774, 22.0 ],
					"text" : "/RegeneratorNo 2"
				}

			}
, 			{
				"box" : 				{
					"annotation" : "",
					"fontface" : 1,
					"fontsize" : 20.0,
					"id" : "obj-114",
					"linecount" : 2,
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 273.526311874389648, 70.578946352005005, 191.0, 52.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 579.188106387853622, 99.0, 205.128192901611328, 34.615382552146912 ],
					"text" : "Recording Strategy",
					"textcolor" : [ 1.0, 0.843137254901961, 0.090196078431373, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-21",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 333.921049833297729, 214.473682165145874, 50.0, 22.0 ],
					"text" : "Mixed"
				}

			}
, 			{
				"box" : 				{
					"activebgcolor" : [ 1.0, 0.709803921568627, 0.196078431372549, 1.0 ],
					"fontsize" : 25.0,
					"id" : "obj-7",
					"maxclass" : "live.menu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "float" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 288.157891988754272, 134.210525035858154, 110.526315689086914, 33.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 299.184207677841187, 139.743581414222717, 110.526315689086914, 33.0 ],
					"saved_attribute_attributes" : 					{
						"activebgcolor" : 						{
							"expression" : "themecolor.live_lcd_control_fg"
						}
,
						"textcolor" : 						{
							"expression" : "themecolor.live_arranger_grid_tiles"
						}
,
						"valueof" : 						{
							"parameter_enum" : [ "LLM", "Markov", "Mixed", "Dummy" ],
							"parameter_longname" : "live.menu",
							"parameter_mmax" : 3,
							"parameter_modmode" : 0,
							"parameter_shortname" : "live.menu",
							"parameter_type" : 2,
							"parameter_unitstyle" : 9
						}

					}
,
					"textcolor" : [ 0.039216, 0.039216, 0.039216, 1.0 ],
					"varname" : "live.menu"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.0, 0.729411764705882, 1.0, 1.0 ],
					"fontface" : 1,
					"fontsize" : 30.0,
					"id" : "obj-196",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 399.999996185302734, 6.578947305679321, 379.0, 41.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 659.999984264373779, 24.999999403953552, 210.975614786148071, 41.0 ],
					"text" : "Duetable - UI",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-6",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 288.157891988754272, 448.684206247329712, 119.0, 23.0 ],
					"text" : "/RegeneratorNo $1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-17",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 293.421049833297729, 690.789467096328735, 405.263154029846191, 22.0 ],
					"text" : "udpsend 127.0.0.1 12345"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-57",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 0.0, 163.0, 105.0, 22.0 ],
					"text" : "OSC-route /gyro/z"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-28",
					"linecount" : 2,
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "OSCTimeTag" ],
					"patching_rect" : [ 24.0, 0.0, 98.0, 36.0 ],
					"text" : "OpenSoundControl"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"background" : 1,
					"grad1" : [ 0.298039215686275, 0.203921568627451, 0.203921568627451, 1.0 ],
					"grad2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"id" : "obj-120",
					"maxclass" : "panel",
					"mode" : 1,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1638.333294987678528, 399.999991178512573, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 1172.56646603345871, 94.690273106098175, 4.424779117107391, 287.610642611980438 ],
					"proportion" : 0.5,
					"rounded" : 0
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"background" : 1,
					"grad1" : [ 0.298039215686275, 0.203921568627451, 0.203921568627451, 1.0 ],
					"grad2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"id" : "obj-119",
					"maxclass" : "panel",
					"mode" : 1,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1623.333294987678528, 384.999991178512573, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 854.86732542514801, 379.646048247814178, 322.123919725418091, 4.0 ],
					"proportion" : 0.5,
					"rounded" : 0
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"background" : 1,
					"grad1" : [ 0.298039215686275, 0.203921568627451, 0.203921568627451, 1.0 ],
					"grad2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"id" : "obj-118",
					"maxclass" : "panel",
					"mode" : 1,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1698.333293199539185, 219.999995112419128, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 504.858383536338806, 234.241874635219574, 353.787638604640961, 4.424779117107391 ],
					"proportion" : 0.5,
					"rounded" : 0
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"background" : 1,
					"grad1" : [ 0.298039215686275, 0.203921568627451, 0.203921568627451, 1.0 ],
					"grad2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"id" : "obj-117",
					"maxclass" : "panel",
					"mode" : 1,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1608.333294987678528, 369.999991178512573, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 854.646022140979767, 99.0, 4.0, 282.300907671451569 ],
					"proportion" : 0.5,
					"rounded" : 0
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"background" : 1,
					"grad1" : [ 0.298039215686275, 0.203921568627451, 0.203921568627451, 1.0 ],
					"grad2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"id" : "obj-116",
					"maxclass" : "panel",
					"mode" : 1,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1683.333293199539185, 204.999995112419128, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 500.884996056556702, 90.265493988990784, 4.255319118499756, 193.333328723907471 ],
					"proportion" : 0.5,
					"rounded" : 0
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"background" : 1,
					"grad1" : [ 0.298039215686275, 0.203921568627451, 0.203921568627451, 1.0 ],
					"grad2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"id" : "obj-1",
					"maxclass" : "panel",
					"mode" : 1,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1494.871705770492554, 137.913465619087219, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 227.631576776504517, 280.687589287757874, 277.508738398551941, 4.0 ],
					"proportion" : 0.5,
					"rounded" : 0
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"background" : 1,
					"bgcolor" : [ 1.0, 0.145098039215686, 0.0, 1.0 ],
					"id" : "obj-2",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 228.333327889442444, -4.99999988079071, 1703.389751315116882, 1086.440627455711365 ],
					"presentation" : 1,
					"presentation_rect" : [ 227.631576776504517, 2.631578922271729, 1703.389751315116882, 1086.440627455711365 ],
					"proportion" : 0.5
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 1 ],
					"order" : 0,
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 0 ],
					"order" : 1,
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-96", 0 ],
					"source" : [ "obj-105", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-96", 1 ],
					"source" : [ "obj-107", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-111", 1 ],
					"order" : 0,
					"source" : [ "obj-109", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-111", 0 ],
					"order" : 1,
					"source" : [ "obj-109", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-53", 0 ],
					"source" : [ "obj-111", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-89", 0 ],
					"order" : 1,
					"source" : [ "obj-112", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-90", 0 ],
					"order" : 0,
					"source" : [ "obj-112", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-131", 0 ],
					"order" : 0,
					"source" : [ "obj-129", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-144", 0 ],
					"order" : 1,
					"source" : [ "obj-129", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-147", 0 ],
					"order" : 2,
					"source" : [ "obj-129", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-135", 0 ],
					"order" : 0,
					"source" : [ "obj-130", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-147", 1 ],
					"order" : 2,
					"source" : [ "obj-130", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-151", 0 ],
					"order" : 1,
					"source" : [ "obj-130", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-133", 0 ],
					"source" : [ "obj-131", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-134", 0 ],
					"source" : [ "obj-135", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-130", 0 ],
					"source" : [ "obj-144", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-149", 0 ],
					"source" : [ "obj-147", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-147", 0 ],
					"source" : [ "obj-151", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 0 ],
					"source" : [ "obj-18", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 0 ],
					"source" : [ "obj-19", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 0 ],
					"source" : [ "obj-20", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 0 ],
					"source" : [ "obj-22", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"source" : [ "obj-26", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"source" : [ "obj-30", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-49", 0 ],
					"order" : 1,
					"source" : [ "obj-31", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-50", 1 ],
					"order" : 0,
					"source" : [ "obj-31", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-50", 0 ],
					"order" : 1,
					"source" : [ "obj-31", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-62", 0 ],
					"order" : 0,
					"source" : [ "obj-31", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 0 ],
					"source" : [ "obj-32", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-40", 0 ],
					"source" : [ "obj-34", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-18", 0 ],
					"order" : 0,
					"source" : [ "obj-36", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-20", 0 ],
					"order" : 1,
					"source" : [ "obj-36", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 0 ],
					"source" : [ "obj-40", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-19", 0 ],
					"order" : 0,
					"source" : [ "obj-41", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-22", 0 ],
					"order" : 1,
					"source" : [ "obj-41", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-46", 0 ],
					"source" : [ "obj-43", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 0 ],
					"source" : [ "obj-46", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-36", 0 ],
					"source" : [ "obj-47", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-51", 0 ],
					"source" : [ "obj-49", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-52", 1 ],
					"order" : 0,
					"source" : [ "obj-51", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-53", 0 ],
					"order" : 1,
					"source" : [ "obj-51", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-17", 0 ],
					"order" : 1,
					"source" : [ "obj-54", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-56", 1 ],
					"order" : 0,
					"source" : [ "obj-54", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-36", 0 ],
					"source" : [ "obj-55", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-41", 0 ],
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-41", 0 ],
					"source" : [ "obj-59", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-27", 1 ],
					"order" : 0,
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-53", 0 ],
					"order" : 1,
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-87", 0 ],
					"source" : [ "obj-61", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-61", 0 ],
					"source" : [ "obj-66", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-79", 0 ],
					"order" : 1,
					"source" : [ "obj-69", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-81", 0 ],
					"order" : 0,
					"source" : [ "obj-69", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-21", 1 ],
					"order" : 0,
					"source" : [ "obj-7", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-21", 0 ],
					"order" : 1,
					"source" : [ "obj-7", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"order" : 0,
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-47", 0 ],
					"order" : 4,
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-55", 0 ],
					"order" : 3,
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-58", 0 ],
					"order" : 2,
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-59", 0 ],
					"order" : 1,
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-74", 0 ],
					"source" : [ "obj-72", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-53", 0 ],
					"source" : [ "obj-74", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-83", 0 ],
					"source" : [ "obj-77", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-86", 0 ],
					"source" : [ "obj-79", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-84", 0 ],
					"source" : [ "obj-81", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-77", 0 ],
					"source" : [ "obj-82", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-53", 0 ],
					"source" : [ "obj-83", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-53", 0 ],
					"source" : [ "obj-84", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-53", 0 ],
					"source" : [ "obj-87", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-107", 0 ],
					"order" : 0,
					"source" : [ "obj-89", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-92", 1 ],
					"order" : 1,
					"source" : [ "obj-89", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-92", 0 ],
					"order" : 2,
					"source" : [ "obj-89", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-107", 1 ],
					"order" : 0,
					"source" : [ "obj-90", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-107", 0 ],
					"order" : 1,
					"source" : [ "obj-90", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-96", 0 ],
					"source" : [ "obj-92", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-98", 1 ],
					"order" : 0,
					"source" : [ "obj-96", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-98", 0 ],
					"order" : 1,
					"source" : [ "obj-96", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-109", 0 ],
					"source" : [ "obj-98", 0 ]
				}

			}
 ],
		"parameters" : 		{
			"obj-31" : [ "live.menu[1]", "live.menu", 0 ],
			"obj-43" : [ "live.menu[3]", "live.menu", 0 ],
			"obj-62" : [ "live.menu[2]", "live.menu", 0 ],
			"obj-7" : [ "live.menu", "live.menu", 0 ],
			"obj-89" : [ "live.menu[4]", "live.menu", 0 ],
			"obj-90" : [ "live.menu[5]", "live.menu", 0 ],
			"parameterbanks" : 			{
				"0" : 				{
					"index" : 0,
					"name" : "",
					"parameters" : [ "-", "-", "-", "-", "-", "-", "-", "-" ]
				}

			}
,
			"inherited_shortname" : 1
		}
,
		"dependency_cache" : [ 			{
				"name" : "OSC-route.mxe64",
				"type" : "mx64"
			}
, 			{
				"name" : "OpenSoundControl.mxe64",
				"type" : "mx64"
			}
 ],
		"autosave" : 0
	}

}
