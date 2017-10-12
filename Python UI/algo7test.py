#cube.faces[cube.facenames[0]].squares[0][0] left (red)
#cube.faces[cube.facenames[1]].squares[0][0] front (white)
#cube.faces[cube.facenames[2]].squares[0][0] right (orange)
#cube.faces[cube.facenames[3]].squares[0][0] back (yellow)
#cube.faces[cube.facenames[4]].squares[0][0] bottom (blue)
#cube.faces[cube.facenames[5]].squares[0][0] top (green)

# Green first, then red, then yellow.

if not vars.algo7: # This algorithm is basicly a repeat of algorithm two with some minor changes
	# Check which color is in what spot (the corner between red - yellow - green)
	# If the colors match whichever two surround it on the same vertical layer (left - right) then turn the cube counter-clockwise
		# If no incorrectly positioned corners are found end the algorithm by setting vars.solved to true
	# Elif the colors do not match the two adjacant colors
		# Add 'RDrd' as many times as needed to make the colors match the ones adjacant.  (Amount of executions based on position of the colors), add a counter-clockwise turn at the end of this