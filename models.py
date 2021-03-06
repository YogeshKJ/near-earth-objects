"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation='', name=None, diameter=float('nan'), hazardous=False):
        """Create a new `NearEarthObject`.

        :param
        designation: The primary designation for this NearEarthObject. Default: ''
        name: The IAU name for this NearEarthObject. Default: None
        diameter: The diameter, in kilometers, of this NearEarthObject. Default: float('nan')
        hazardous: Whether or not this NearEarthObject is potentially hazardous. Default: False
        approaches: A collection of this NearEarthObjects close approaches to Earth. Default: []
        """
        # onto attributes named `designation`, `name`, `diameter`, and `hazardous`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases, such as a empty name being represented by `None`
        # and a missing diameter being represented by `float('nan')`.
        self.designation = designation
        self.name = name if name else None
        self.diameter = float(diameter) if diameter else float('nan')
        self.hazardous = True if hazardous == 'Y' else False

        # Create an empty initial collection of linked approaches.
        self.approaches = set()

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name:
            return f'{self.designation} {self.name}'
        else:
            return f'{self.designation}'

    def __str__(self):
        """Return `str(self)`."""
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        if self.diameter:
            if self.hazardous:
                return f"NEO {self.fullname!r} has a diameter of {self.diameter: .3f} and is potentially hazardous!"
            else:
                return f"NEO {self.fullname!r} has a diameter of {self.diameter: .3f} and is NOT potentially hazardous!"
        else:
            if self.hazardous:
                return f"NEO {self.fullname!r} has an unknown diameter and is potentially hazardous!"

            else:
                return f"NEO {self.fullname!r} has an unknown diameter and is NOT potentially hazardous!"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    # If you make changes, be sure to update the comments in this file.

    def __init__(self, _designation='', time=None, distance=0.0, velocity=0.0):
        """Create a new `CloseApproach`.

        :param 
        _designation: The primary designation for this NearEarthObject. Default: ''
        time: The date and time, in UTC, at which the NEO passes closest to Earth. Default: None
        distance: The nominal approach distance, in astronomical units, of the NEO to Earth at the closest point.
        Default = 0.0
        velocity: The velocity, in kilometers per second, of the NEO relative to Earth at the closest point.
        Default = 0.0
        neo: The NearEarthObject that is making a close approach to Earth. Default = None
        """
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.
        self._designation = _designation
        self.time = cd_to_datetime(time) if time else None
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # build a formatted representation of the approach time.
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.

        if self.time_str:
            if self.distance:
                if self.velocity:
                    return f"At {self.time_str}, {self.neo.fullname} " \
                           f"approaches Earth at a distance of {self.distance:.2f} " \
                           f"au and a velocity of {self.velocity:.2f} km/s!"
                else:
                    return f"At {self.time_str}, {self.neo.fullname} " \
                           f"approaches Earth at a distance of {self.distance:.2f} au with an unknown velocity!"
            else:
                if self.velocity:
                    return f"At {self.time_str}, {self.neo.fullname} " \
                           f"approaches Earth at an unknown distance with a velocity of {self.velocity:.2f} km/s!"
                else:
                    return f"At {self.time_str}, {self.neo.fullname} " \
                           f"approaches Earth at an unknown distance and an unknown velocity!"

        else:
            return "No known close approach !!"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
