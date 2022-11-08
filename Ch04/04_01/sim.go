package main

import "fmt"

type Location struct {
	Lat float64
	Lng float64
}

func NewLocation(lat, lng float64) (Location, error) {
	if lat < -90 || lat > 90 {
		return Location{}, fmt.Errorf("invalid lat: %#v", lat)
	}
	if lng < -180 || lng > 180 {
		return Location{}, fmt.Errorf("invalid lng: %#v", lng)
	}

	loc := Location{
		Lat: lat,
		Lng: lng,
	}
	return loc, nil
}

func main() {
	loc, err := NewLocation(32.5253837, 34.9427434)
	if err != nil {
		fmt.Println("ERROR:", err)
		return
	}
	fmt.Println(loc)
}
