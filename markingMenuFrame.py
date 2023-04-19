import maya.cmds as cmds
import maya.OpenMaya as openMaya

#
# PURPOSE :
# create markingMenu and this practice will help to write some lines of code
# efficiently, also make more durable and sustainable codes as this practice 
# 

#
# Step 1. making the frame of marking menu
# SOURCE COMMANDS : popupMenu, menuItem,  
# popupMenu : https://help.autodesk.com/view/MAYAUL/2022/ENU/index.html?contextId=COMMANDSPYTHON-POPUPMENU
# menuItem  : https://help.autodesk.com/view/MAYAUL/2022/ENU/?guid=__CommandsPython_index_html
#


# button 1:left 2:middle 3:right
# parent = "viewPanes" is important attributes for making markingMenu

cmds.popupMenu(markingMenu = True,
               ctrlModifier=True,
               altModifier=True,
               shiftModifier=False,
               button=1,
               parent="viewPanes"
               )

# cheking how to parent to popupMenu
cmds.menuItem( label='Red', radialPosition = "N" )
cmds.menuItem( label='Orange', radialPosition = "NW")
cmds.menuItem( label='Yellow', radialPosition = "W")
cmds.menuItem( label='Green', radialPosition = "SW")
cmds.menuItem( label='Blue', radialPosition = "S")
cmds.menuItem( label='DarkBlue', radialPosition = "SE")
cmds.menuItem( label='Purple', radialPosition = "E")
cmds.menuItem( label='Rainbow', radialPosition = "NE")