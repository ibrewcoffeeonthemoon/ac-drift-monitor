from typing import Any, Callable


def addButton(object: Any, text: str) -> int:
    ...


def addCheckBox(object: Any, title: str) -> int:
    ...


def addGraph(object: Any, title: str) -> int:
    ...


def addItem(object: Any, name: str) -> int:
    ...


def addLabel(window: Any, name: str) -> int:
    ...


def addListBox(object: Any, title: str) -> int:
    ...


def addOnAppActivatedListener(object: Any, function: Callable) -> int:
    ...


def addOnAppDismissedListener(object: Any, function: Callable) -> int:
    ...


def addOnChatMessageListener(object: Any, function: Callable) -> int:
    ...


def addOnCheckBoxChanged(object: Any, function: Callable) -> int:
    ...


def addOnClickedListener(object: Any, function: Callable) -> int:
    ...


def addOnListBoxDeselectionListener(object: Any, function: Callable) -> int:
    ...


def addOnListBoxSelectionListener(object: Any, function: Callable) -> int:
    ...


def addOnValidateListener(object: Any, function: Callable) -> int:
    ...


def addOnValueChangeListener(object: Any, function: Callable) -> int:
    ...


def addProgressBar(object: Any, title: str) -> int:
    ...


def addRenderCallback(object: Any, function: Callable) -> int:
    ...


def addSerieToGraph(object: Any, r: float, g: float, b: float) -> int:
    ...


def addSpinner(object: Any, title: str) -> int:
    ...


def addTextBox(object: Any, title: str) -> int:
    ...


def addTextInput(object: Any, text: str) -> int:
    ...


def addValueToGraph(object: Any, serieId: int, value: float) -> int:
    ...


def console(msg: str) -> int:
    ...


def drawBackground(object: Any, visibility: bool) -> int:
    ...


def drawBorder(object: Any, visibility: bool) -> int:
    ...


def freeCameraMoveForward(self) -> int:
    ...


def freeCameraMoveRight(self) -> int:
    ...


def freeCameraMoveUpWorld(self) -> int:
    ...


def freeCameraRotateHeading(self) -> int:
    ...


def freeCameraRotatePitch(self) -> int:
    ...


def freeCameraRotateRoll(self) -> int:
    ...


def freeCameraSetClearColor(self) -> int:
    ...


def getCameraMode(self) -> int:
    ...


def getCarLeaderboardPosition(carId: int) -> int:
    ...


def getCarMinHeight(carId: int) -> float:
    ...


def getCarName(carId: int) -> str:
    ...


def getCarRealTimeLeaderboardPosition(carId: int) -> int:
    ...


def getCarState(carId: int, infoId: int, param: str = "") -> Any:
    ...


def getCarsCount(self) -> int:
    ...


def getCurrentSplits(carId: int) -> tuple[float, float, float]:
    ...


def getDriverName(carId: int) -> str:
    ...


def getFocusedCar() -> int:
    ...


def getItemCount(object: Any) -> int:
    ...


def getLastSplits(carId: int) -> tuple[float, float, float]:
    ...


def getPosition(object: Any) -> tuple[float, float]:
    ...


def getSelectedItems(object: Any) -> int:
    ...


def getSize(object: Any) -> tuple[int, int]:
    ...


def getText(object: Any) -> str:
    ...


def getTrackConfiguration(carId: int) -> str:
    ...


def getTrackName(carId: int) -> str:
    ...


def getValue(object: Any) -> int:
    ...


def glBegin(drawType: int) -> int:
    ...


def glColor3f(r: float, g: float, b: float) -> int:
    ...


def glColor4f(r: float, g: float, b: float, a: float) -> int:
    ...


def glEnd() -> int:
    ...


def glQuad(xPos: float, yPos: float, width: float, height: float) -> int:
    ...


def glQuadTextured(xPos: float, yPos: float, width: float, height: float, texId: int) -> int:
    ...


def glVertex2f(xPos: float, yPos: float) -> int:
    ...


def highlightListBoxItem(object: Any, id: int) -> int:
    ...


def isAcLive(self) -> bool:
    ...


def isCameraOnBoard(self) -> bool:
    ...


def log(msg: str) -> int:
    ...


def newApp(appName: str) -> int:
    ...


def newTexture(path: str) -> int:
    ...


def removeItem(object: Any, id: int) -> int:
    ...


def sendChatMessage(msg: str) -> int:
    ...


def setAllowDeselection(object: Any, allow: bool) -> int:
    ...


def setAllowMultiSelection(object: Any, allow: bool) -> int:
    ...


def setBackgroundColor(object: Any, r: float, g: float, b: float) -> int:
    ...


def setBackgroundOpacity(object: Any, opacity: float) -> int:
    ...


def setBackgroundTexture(object: Any, texture: str) -> int:
    ...


def setCameraMode(mode: int) -> int:
    ...


def setFocus(object: Any, focus: bool) -> int:
    ...


def setFont(object: Any, font: str) -> int:
    ...


def setFontAlignment(object: Any, alignment: str) -> int:
    ...


def setFontColor(object: Any, r: float, g: float, b: float, a: float) -> int:
    ...


def setFontSize(object: Any, size: float) -> int:
    ...


def setIconPosition(object: Any, xPos: float, yPos: float) -> int:
    ...


def setItemNumberPerPage(object: Any, numItems: int) -> int:
    ...


def setPosition(object: Any, xPos: float, yPos: float) -> int:
    ...


def setRange(min: float, max: float, maxPoint: float = 0.0) -> int:
    ...


def setSize(object: Any, width: int, height: int) -> int:
    ...


def setStep(object: Any, step: float) -> int:
    ...


def setText(object: Any, text: str) -> int:
    ...


def setTitle(object: Any, title: str) -> int:
    ...


def setTitlePosition(object: Any, xPos: float, yPos: float) -> int:
    ...


def setValue(object: Any, value: float) -> int:
    ...


def setVisible(object: Any, visible: bool) -> int:
    ...


"""
Python Apps – New functions
leBluem edited this page on Aug 31, 2024 · 7 revisions
CSP adds some new functions for Python apps, and here is the full list of them with argument names and return types. Each time function requires a vector argument, such as vec2, vec3 or vec4, you can pass either a corresponding amount of numbers directly, or pass them packed in a tuple.

See also official and inofficial python docs: https://assettocorsamods.net/threads/doc-python-doc.59/ Shared memory reference: https://assettocorsamods.net/threads/doc-shared-memory-reference.58/ A getting started guide: https://assettocorsamods.net/threads/getting-started-with-ac-app-developing.716/#post-2892
"""

vec2 = tuple[float, float]
vec3 = tuple[float, float, float]
vec4 = tuple[float, float, float, float]
mat4x4 = tuple[
    tuple[float, float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float],
]


# Track controls:
def ext_applyTrackConfig(config: str, flags: int) -> None:
    # flags: 1<<0 for restore conditions, 1<<1 for partial update
    ...


def ext_setTrackConditionInput(conditionName: str, value: float) -> None:
    ...


# Mirrors (requires Real Mirror enabled):
def ext_mirrorLeft() -> None:
    ...


def ext_mirrorRight() -> None:
    ...


def ext_mirrorUp() -> None:
    ...


def ext_mirrorDown() -> None:
    ...


def ext_mirrorFovUp() -> None:
    ...


def ext_mirrorFovDown() -> None:
    ...


def ext_mirrorAspectRatioUp() -> None:
    ...


def ext_mirrorAspectRatioDown() -> None:
    ...


def ext_mirrorToggleMon() -> None:
    ...


def ext_mirrorPrev() -> None:
    ...


def ext_mirrorNext() -> None:
    ...


def ext_mirrorCurrent() -> int:
    ...


def ext_mirrorParams() -> tuple[bool, float, float, int, int]:
    # returns: (isMonitor: bool, fov: float, aspectMult: float, role: int, index: int):
    ...


# Flipping mirrors (available since 0.1.76, 1 for horizontal flip, 2 for vertical, 3 for both):
def ext_mirrorGetFlip() -> int:
    ...


def ext_mirrorSetFlip(flip: int) -> int:
    ...


# G27 LEDs:
def ext_isG27Available() -> bool:
    ...


def ext_setG27Thresholds(minRpm: float, maxRpm: float) -> None:
    ...


# General functions:
def ext_patchVersion() -> str:
    ...


def ext_patchVersionCode() -> int:
    ...


def ext_weatherDebugText() -> str:
    ...


def ext_setStrictMode() -> None:    # ivates strict mode with better error reporting, recommended
    ...


def ext_pauseWhenHidden() -> None:  # allows app to pause when it’s not ive
    ...


def ext_isAnyAppVisible() -> bool:
    ...


def ext_isAppVisible(appName: str) -> bool:
    ...


def ext_perfBegin(key: str | None):
    # starts measuring time
    ...


def ext_perfEnd(key: str | None) -> float:
    # stops measuring time, returns time in milliseconds, shows it in Python Debug app
    ...


def ext_loadIniFileAsJson(filename: str, includeDir0: str | None, includeDir1: str | None, includeDir2: str | None) -> str:
    # question mark means parameter is optional
    ...


def ext_parseIniAsJson(iniData: str) -> str:
    ...


def ext_getBaseAltitude() -> float:
    ...


def ext_getAltitude(car: int) -> float:
    ...


def ext_setDriverVisible(visible: bool, carIndex: int) -> None:
    ...


def ext_setDoorsOpen(doorOpen: bool, carIndex: int) -> None:
    ...


def ext_isExtendedPhysics(car: int) -> bool:
    ...


def ext_getTyreGrain(car: int, tyre: int) -> float:
    ...


def ext_getHeadlights(car: int) -> bool:
    ...


def ext_getHandbrake(car: int) -> float:
    ...


def ext_getTyreIsHot(car: int, tyre: int) -> bool:
    ...


def ext_getTyreTempMult(car: int, tyre: int) -> float:
    ...


def ext_getTyreBlister(car: int, tyre: int) -> float:
    ...


def ext_getTyreFlatSpot(car: int, tyre: int) -> float:
    ...


def ext_getTyreVirtualKM(car: int, tyre: int) -> float:
    ...


def ext_getTyreCarcassTemp(car: int, tyre: int) -> float:
    ...


def ext_getSuspensionTravel(corner: int) -> float:  # ! broken until and including csp 0.1.77-prev80
    ...


def ext_getDamperTravel(corner: int) -> float:      # ! broken until and including csp 0.1.77-prev80
    ...


def ext_getTcSetting1(car: int) -> int:
    ...


def ext_getTcSetting2() -> int:
    ...


def ext_getAeroSpeed() -> float:
    ...


def ext_getDrag() -> float:
    ...


def ext_getDownforce(selection: int) -> float:
    ...


def ext_getStaticDeflection() -> float:
    ...


def ext_getCurrentTorque() -> float:
    ...


def ext_getBrakeCoreTemp(corner: int) -> float:
    ...


def ext_getSteerTorque() -> float:
    ...


def ext_getBrakeTorque(corner: int) -> float:
    ...


def ext_getTireLoadedRadius(corner: int) -> float:
    ...


def ext_isTripleScreenCamera() -> bool:
    ...


def ext_isInVR() -> bool:
    ...


def ext_getCameraDirection() -> vec3:  # vec3 is a tuple with 3 elements
    ...


def ext_getCameraPosition() -> vec3:
    ...


def ext_setCameraPosition(pos: vec3):
    ...


def ext_getCameraPositionAxis(axis: int) -> float:
    ...


def ext_setCameraPositionAxis(axis: int, value: float) -> None:
    ...


def ext_setCameraDirection(forward: vec3, up: vec3 | None) -> None:
    ...


def ext_getCameraMatrix() -> mat4x4:  # mat4x4 is a tuple with 16 elements
    ...


def ext_getCameraRollRad() -> float:  # rad means result is in radians
    ...


def ext_getCameraPitchRad() -> float:
    ...


def ext_getCameraYawRad() -> float:
    ...


def ext_getCameraFov() -> float:
    ...


def ext_setCameraFov(value: float) -> None:
    ...


def ext_getCameraDofFactor() -> float:
    ...


def ext_setCameraDofFactor(value: float) -> None:
    ...


def ext_getCameraDofFocus() -> float:
    ...


def ext_setCameraDofFocus(value: float) -> None:
    ...


def ext_getCameraClipNear() -> float:
    ...


def ext_setCameraClipNear(value: float) -> None:
    ...


def ext_getCameraClipFar() -> float:
    ...


def ext_setCameraClipFar(value: float) -> None:
    ...


def ext_currentPpFilter() -> str:
    ...


def ext_getReplayFrameMS() -> float:  # frame time in ms
    ...


def ext_getReplayFrames() -> int:     # number of recorded frames
    ...


def ext_getReplayPosition() -> int:   # frame index
    ...


def ext_setReplayPosition(frameIndex: int) -> None:
    ...


def ext_getCurrentCamera() -> int:
    ...


def ext_setCurrentCamera(mode: int) -> None:
    ...


def ext_getCurrentDrivableCamera() -> int:
    ...


def ext_setCurrentDrivableCamera(mode: int) -> None:
    ...


def ext_getTrackCamerasNumber() -> int:
    ...


def ext_getCurrentTrackCamera() -> int:
    ...


def ext_setCurrentTrackCamera(setIndex: int) -> None:
    ...


def ext_getAudioVolume() -> float:
    ...


def ext_setAudioVolume(volume: float) -> None:
    ...


def ext_getPreviousSectorTime() -> str:
    ...


def ext_getCurrentSector() -> int:
    ...


def ext_isButtonPressed(keyIndex: int) -> bool:
    ...


def ext_isCtrlPressed() -> bool:
    ...


def ext_isAltPressed() -> bool:
    ...


def ext_isShiftPressed() -> bool:
    ...


def ext_isJoystickButtonPressed(controllerIndex: int, buttonIndex: int) -> bool:
    ...


def ext_getJoystickAxisValue(controllerIndex: int, axisIndex: int) -> float:
    ...


def ext_getJoystickDpadValue(controllerIndex: int, dpadIndex: int) -> int:
    ...


def ext_setClipboardData(text: str) -> None:
    ...


def ext_isVirtualMirrorForced() -> bool:
    ...


def ext_markLapAsSpoiled() -> None:
    ...


def ext_getCameraPositionRelativeToCar() -> vec3:
    ...


def ext_getCompassAngle(direction: vec3) -> float:
  # turns direction into heading angle in degrees
    ...


def ext_dirname() -> str:
  # path to python app folder
    ...


def ext_getSplineLength(splineIndex: int) -> float:
  # 0 for main spline (so, length of the whole track), 1 for pits spline
    ...


def ext_worldToSpline(splineIndex: int, worldPos: vec3) -> float:
    ...


def ext_splineToWorld(splineIndex: int, splinePos: float) -> vec3:
    ...


def ext_storeLua(key: str, value: float | str) -> None:
    ...


def ext_loadLua(key: str) -> float | str:
    ...


def ext_getStateAbs(carIndex: int) -> int:
    ...


def ext_getStateAbsActive(carIndex: int) -> bool:
    ...


def ext_getStateTc(carIndex: int) -> int:
    ...


def ext_getStateTcActive(carIndex: int) -> bool:
    ...


def ext_pauseFsWatching() -> None:
    ...


def ext_resumeFsWatching() -> None:
    ...


def ext_resetCar() -> None:       # resets car to the road invalidating lap
    ...


def ext_takeAStepBack() -> None:  # moves car back invalidating lap
    ...


def ext_weatherFxActive() -> bool:
    ...


def ext_weatherTimeOffset(offset: float) -> bool:
    ...


def ext_getWeatherTimeMult() -> float:
    ...


def ext_setWeatherTimeMult(value: float) -> None:
    ...


def ext_isVaoPatchLoaded() -> bool:
    ...


def ext_vaoOnly() -> None:
    ...


def ext_vaoNormalDebug() -> None:
    ...


def ext_vaoDisable() -> None:
    ...


def ext_vaoNormal() -> None:
    ...


def ext_setVaoActive(active: bool) -> None:
    ...


def ext_getWiperSpeedsNumber() -> int:
    ...


def ext_getWiperSpeed() -> int:
    ...


def ext_setWiperSpeed(wiperSpeed: int) -> None:
    ...


def ext_getCameraProj() -> mat4x4:
    ...


def ext_getCameraView() -> mat4x4:
    ...


def ext_getLightsNum() -> int:
    ...


def ext_getCarLightsNum() -> int:
    ...


def ext_getTrackLightsNum() -> int:
    ...


def ext_getLightsVisible() -> int:
    ...


def ext_getCarLightsVisible() -> int:
    ...


def ext_getTrackLightsVisible() -> int:
    ...


def ext_getLightsMirrorVisible() -> int:
    ...


def ext_getCarLightsMirrorVisible() -> int:
    ...


def ext_getTrackLightsMirrorVisible() -> int:
    ...


def ext_getAmbientMult() -> float:
    ...


def ext_getAngleSpeed() -> float:
    ...


def ext_debugLights(nameFilter: str, count: int, distance: float, mode: int) -> None:
    ...

# Extended render functions:


def ext_glSetCullMode(mode: int) -> None:
  # mode: 0 for front, 1 for back, 2 for no culling, 4 for wireframe, 7 for antialiased wireframe
    ...


def ext_glSetBlendMode(mode: int) -> None:
  # mode: 0 for opaque, 1 for alpha blend, 2 for alpha test, 4 for additive, 5 for multiplicative
    ...


def ext_mirrorTexture() -> int:
  # returns texture index which can be used the same as createTexture()
    ...


def ext_releaseMirrorTexture() -> None:
  # call it for each call of ext_mirrorTexture() when texture is no longer needed to re-activate
  # real mirrors
    ...


def ext_createRenderTarget(width: int, height: int, mips: bool) -> int:
  # returns texture index, but also this number can be used to draw things to
    ...


def ext_clearRenderTarget(rtIndex: int) -> None:
    ...


def ext_generateMips(rtIndex: int) -> None:
    ...


def ext_disposeRenderTarget(rtIndex: int) -> None:
    ...


def ext_bindRenderTarget(rtIndex: int) -> None:
  # starts drawing into render target
    ...


def ext_restoreRenderTarget() -> None:
  # restores original render target to continue drawing app to
    ...


def ext_glSetTexture(textureIndex: int, slotIndex: int) -> None:
  # binds texture
    ...


def ext_glLoadPixelShader(filename: str) -> int:
  # loads pixel shader (there is an example at the bottom of this post)
    ...


def ext_glSetPixelShader(shaderIndex: int) -> None:
  # custom shader will be used for further draw calls
    ...


def ext_glResetPixelShader() -> None:
  # reverts to original pixel shader
    ...


def ext_glVertexTex(posUV: vec4) -> None:
  # adds a new vertex with texture coordinates, use with glBegin() and glEnd()
  # vec4 is a tuple with four values
    ...


def ext_glTexCoord2f(uv: vec2) -> None:
  # adds texture coordinates to previously added vertex
  # vec2 is a tuple with two values
    ...


def ext_glFontCreate(font: str, size: float, italic: int, weight: int) -> int:
    ...


def ext_glFontColor(fontIndex: int, color: vec4) -> None:
    ...


def ext_glFontUse(fontIndex: int, text: str, pos: vec2, scale: float, alignment: int) -> None:
    # uses created font to draw some text
    # alignment: 0 for left, 1 for right, 2 for center
    ...
