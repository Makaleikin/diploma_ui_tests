from dataclasses import dataclass
from enum import Enum


class Range(Enum):
    ModelS_range: str = '396\nmi\nRange (EPA est.)'
    Model3_range: str = '358\nmi\nRange (EPA est.)'
    ModelX_range: str = '333\nmi\nRange\n(EPA est.)'


class Boost(Enum):
    ModelS_boost: str = '1.99\ns\n0-60 mph*'
    Model3_boost: str = '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n.\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\ns\n0-60 mph*'
    ModelX_boost: str = '2.5\ns\n0-60 mph*'


class Model(Enum):
    Model_S: str = 'Model S'
    Model_3: str = 'Model 3'
    Model_X: str = 'Model X'


class Speed(Enum):
    ModelS_speed: str = '200\nmph\nTop Speed†'


class Power(Enum):
    ModelS_power: str = '1,020\nhp\nPeak Power'
    ModelX_power: str = '1,020\nhp\nPeak Power'


class Drive(Enum):
    Model3_drive: str = 'AWD\nDual Motor'


class BoostQuarterMile(Enum):
    ModelX_boost_quarter_mile: str = '9.9\ns\n1/4 Mile'


@dataclass
class Tesla:
    model: Model
    range: Range
    boost: Boost
    speed: Speed
    power: Power
    drive: Drive
    boost_quarter: BoostQuarterMile


model_s = Tesla(model=Model.Model_S,
                range=Range.ModelS_range,
                boost=Boost.ModelS_boost,
                speed=Speed.ModelS_speed,
                power=Power.ModelS_power,
                drive='',
                boost_quarter='')

model_3 = Tesla(model=Model.Model_3,
                range=Range.Model3_range,
                boost=Boost.Model3_boost,
                speed='',
                power='',
                drive=Drive.Model3_drive,
                boost_quarter='')

model_x = Tesla(model=Model.Model_X,
                range=Range.ModelX_range,
                boost=Boost.ModelX_boost,
                speed='',
                power=Power.ModelX_power,
                drive='',
                boost_quarter=BoostQuarterMile.ModelX_boost_quarter_mile)
