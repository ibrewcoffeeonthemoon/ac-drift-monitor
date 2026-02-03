import typing

# GL: Constants for glBegin


class GL:
    Lines: int
    LineStrip: int
    Triangles: int
    Quads: int


# CS: Constants for getCarState parameters
class CS:
    SpeedMS: int
    SpeedMPH: int
    SpeedKMH: int
    Gas: int
    Brake: int
    Clutch: int
    Gear: int
    Aero: int
    BestLap: int
    CamberRad: int
    AccG: int
    CGHeight: int
    DriftBestLap: int
    DriftLastLap: int
    DriftPoints: int
    DriveTrainSpeed: int
    DY: int
    RPM: int
    Load: int
    InstantDrift: int
    IsDriftInvalid: int
    IsEngineLimiterOn: int
    LapCount: int
    LapInvalidated: int
    LapTime: int
    LastFF: int
    LastLap: int
    LocalAngularVelocity: int
    LocalVelocity: int
    Mz: int
    NdSlip: int
    NormalizedSplinePosition: int
    PerformanceMeter: int
    SlipAngle: int
    SlipAngleContactPatch: int
    SlipRatio: int
    SpeedTotal: int
    Steer: int
    SuspensionTravel: int
    TurboBoost: int
    TyreDirtyLevel: int
    TyreContactNormal: int
    TyreContactPoint: int
    TyreHeadingVector: int
    TyreLoadedRadius: int
    TyreRadius: int
    TyreRightVector: int
    TyreSlip: int
    TyreSurfaceDef: int
    TyreVelocity: int
    Velocity: int
    WheelAngularSpeed: int
    WorldPosition: int
    Caster: int
    CurrentTyresCoreTemp: int
    LastTyresTemp: int
    DynamicPressure: int
    RideHeight: int
    ToeInDeg: int
    CamberDeg: int
    KersCharge: int
    KersInput: int
    DrsAvailable: int
    DrsEnabled: int
    EngineBrake: int
    ERSRecovery: int
    ERSDelivery: int
    ERSHeatCharging: int
    ERSCurrentKJ: int
    ERSMaxJ: int
    RaceFinished: int
    P2PStatus: int
    P2PActivations: int


# WHEELS: Constants for wheel identifiers
class WHEELS:
    FL: int
    FR: int
    RL: int
    RR: int


# AERO: Constants for Aero parameters
class AERO:
    CD: int
    CL_Front: int
    CL_Rear: int


# CM: Constants for Camera Modes
class CM:
    Cockpit: int
    Car: int
    Drivable: int
    Track: int
    Helicopter: int
    OnBoardFree: int
    Free: int
    Random: int
    ImageGeneratorCamera: int
    Start: int


# ############# MATH ############
class Vec2f:
    x: float
    y: float

    def __init__(self, x: float = 0, y: float = 0) -> None:
        ...

    def __add__(self, other: "Vec2f") -> "Vec2f":
        ...

    def __sub__(self, other: "Vec2f") -> "Vec2f":
        ...

    def normalize(self) -> None:
        ...

    def __mul__(self, val: float) -> "Vec2f":
        ...
