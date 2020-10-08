
roslaunch robot1_description display.launch model:="$(rospack find robot1_description)/urdf/robot1.urdf" gui:=true


rosrun xacro xacro [arcvivo.xacro] > [archivo_destino.urdf]
rosrun xacro xacro robot1.xacro > robot1_processed.urdf