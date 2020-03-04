import pytest
from airport import Airport
from airport import Plane

airport = Airport()
plane = Plane()

def test_is_full():
    assert airport.is_full() == False

def test_hangar():
    assert len(airport.hangar) == 0

def test_capacity():
    assert airport.capacity == 2

def test_land():
    assert airport.land(plane) == plane

def test_land_full():
    airport.land(plane)
    airport.land(plane)
    assert len(airport.hangar) == 2

def test_airport_full():
    assert airport.is_full() == True

def test_takeoff():
    assert airport.takeoff(plane) == plane

def test_takeoff_hangar():
    airport.takeoff(plane)
    assert len(airport.hangar) == 0
