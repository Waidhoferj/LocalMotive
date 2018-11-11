/* Changes values of inputted business GPS location and changes it based on user location
 */

function EuclidianCompare(userLoc, businesses) {
	for (i = 0; i < businesses.length; i++) {
		busLat = businesses[i]['location'][0]
		busLon = businesses[i]['location'][1]
		businesses[i]['location'][0] = Math.pow(busLat - userLoc[0]) + Math.pow(busLon - userLoc[1])
	}
	return businesses
}