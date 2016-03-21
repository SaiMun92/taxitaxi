import numpy as np
import math

# Compute Distance using HaversineDistance
def dist(coord1, coord2):
	sin = math.sin
	cos = math.cos
	pi = math.pi
	atan2 = math.atan2
	sqrt = math.sqrt
	R = 6371000 #meters

	lon1, lat1 = coord1
	lon2, lat2 = coord2
    phi1 = lat1 * (3.1415 / 180)
    phi2 = lat2 * (3.1415 / 180)
    Dphi = phi2 - phi1
    Dlambda = (lon2 - lon1) *  (3.1415 / 180)

    a = sin(Dphi / 2) ** 2 + cos(phi1)*cos(phi2) *sin(Dlambda/2)**2
    c = 2 * atan2(sqrt(a),sqrt(1-a))
    d = R * c
    return d



def speeds(polyline):
    N = len(polyline)

    if N == 0:
        return []

    v = [0.]*N
    v[0] = 0
    for i in range(1, N):
        v[i] = ( dist( polyline[i-1] , polyline[i] ) / 15 ) * 3.6 # dist() = haversine distance per second * 3.6

    return v