# SydorenkoG12 - enclosure for the "Yalynka" PCB (Fusion 360 script)
# Fusion 360: Utilities > ADD-INS > Scripts and Add-Ins > "+" (or green +) > select this folder > Run.
# Creates a new design with components "Korpus" (case), "Pidstavka" (stand) and imports the PCB STEP.
# Units in the data: mm. Coordinates: PCB plane = XY (tree upright, +Y up), PCB front = +Z.
import adsk.core, adsk.fusion, traceback, os, math

DATA = {"case":[{"body":"Case floor","z0":0.0,"z1":2.0,"regions":[{"outer":{"p":[[22.5,-2.5],[87.5,-2.5],[87.5,21.5],[110.0,21.5],[111.8238,25.7099],[85.7706,53.5],[98.0,53.5],[100.0,57.5],[79.0,85.5],[88.0,85.5],[89.9085,89.6148],[61.2705,123.46],[48.7295,123.46],[20.0915,89.6148],[22.0,85.5],[31.0,85.5],[10.0,57.5],[12.0,53.5],[24.2294,53.5],[-1.8238,25.7099],[0.0,21.5],[22.5,21.5]]},"holes":[{"c":[22.5,29.0,1.25]},{"c":[88.0,29.0,1.25]},{"c":[48.0,111.5,1.25]},{"c":[62.0,111.5,1.25]},{"c":[51.0,78.5,1.0]},{"c":[51.0,82.5,1.0]},{"c":[51.0,86.5,1.0]},{"c":[55.0,78.5,1.0]},{"c":[55.0,82.5,1.0]},{"c":[55.0,86.5,1.0]},{"c":[59.0,78.5,1.0]},{"c":[59.0,82.5,1.0]},{"c":[59.0,86.5,1.0]}],"area":8375.201}]},{"body":"Case wall","z0":2.0,"z1":4.0,"regions":[{"outer":{"p":[[22.5,-2.5],[87.5,-2.5],[87.5,21.5],[110.0,21.5],[111.8238,25.7099],[85.7706,53.5],[98.0,53.5],[100.0,57.5],[79.0,85.5],[88.0,85.5],[89.9085,89.6148],[61.2705,123.46],[48.7295,123.46],[20.0915,89.6148],[22.0,85.5],[31.0,85.5],[10.0,57.5],[12.0,53.5],[24.2294,53.5],[-1.8238,25.7099],[0.0,21.5],[22.5,21.5]]},"holes":[{"p":[[24.5,23.5],[0.0,23.5],[-0.3648,24.342],[28.8459,55.5],[12.0,55.5],[11.6,56.3],[35.0,87.5],[22.0,87.5],[21.6183,88.323],[49.6571,121.46],[60.3429,121.46],[88.3817,88.323],[88.0,87.5],[75.0,87.5],[98.4,56.3],[98.0,55.5],[81.1541,55.5],[110.3648,24.342],[110.0,23.5],[85.5,23.5],[85.5,-0.5],[24.5,-0.5]]}],"area":940.223}]},{"body":"Case wall","z0":4.0,"z1":5.0,"regions":[{"outer":{"p":[[47.5,-2.5],[87.5,-2.5],[87.5,21.5],[110.0,21.5],[111.8238,25.7099],[85.7706,53.5],[98.0,53.5],[100.0,57.5],[79.0,85.5],[88.0,85.5],[89.9085,89.6148],[61.2705,123.46],[48.7295,123.46],[20.0915,89.6148],[22.0,85.5],[31.0,85.5],[10.0,57.5],[12.0,53.5],[24.2294,53.5],[-1.8238,25.7099],[0.0,21.5],[22.5,21.5],[22.5,-2.5],[29.0,-2.5],[29.0,-0.5],[24.5,-0.5],[24.5,23.5],[0.0,23.5],[-0.3648,24.342],[28.8459,55.5],[12.0,55.5],[11.6,56.3],[35.0,87.5],[22.0,87.5],[21.6183,88.323],[49.6571,121.46],[60.3429,121.46],[88.3817,88.323],[88.0,87.5],[75.0,87.5],[98.4,56.3],[98.0,55.5],[81.1541,55.5],[110.3648,24.342],[110.0,23.5],[85.5,23.5],[85.5,-0.5],[47.5,-0.5]]},"holes":[],"area":903.223},{"outer":{"p":[[42.0,-2.5],[43.5,-2.5],[43.5,-0.5],[42.0,-0.5]]},"holes":[],"area":3.0}]},{"body":"Case wall","z0":5.0,"z1":8.0,"regions":[{"outer":{"p":[[61.0,-2.5],[87.5,-2.5],[87.5,21.5],[110.0,21.5],[111.8238,25.7099],[85.7706,53.5],[98.0,53.5],[100.0,57.5],[79.0,85.5],[88.0,85.5],[89.9085,89.6148],[61.2705,123.46],[48.7295,123.46],[20.0915,89.6148],[22.0,85.5],[31.0,85.5],[10.0,57.5],[12.0,53.5],[24.2294,53.5],[-1.8238,25.7099],[0.0,21.5],[22.5,21.5],[22.5,-2.5],[29.0,-2.5],[29.0,-0.5],[24.5,-0.5],[24.5,23.5],[0.0,23.5],[-0.3648,24.342],[28.8459,55.5],[12.0,55.5],[11.6,56.3],[35.0,87.5],[22.0,87.5],[21.6183,88.323],[49.6571,121.46],[60.3429,121.46],[88.3817,88.323],[88.0,87.5],[75.0,87.5],[98.4,56.3],[98.0,55.5],[81.1541,55.5],[110.3648,24.342],[110.0,23.5],[85.5,23.5],[85.5,-0.5],[61.0,-0.5]]},"holes":[],"area":876.223},{"outer":{"p":[[42.0,-2.5],[43.5,-2.5],[43.5,-0.5],[42.0,-0.5]]},"holes":[],"area":3.0},{"outer":{"p":[[47.5,-2.5],[49.0,-2.5],[49.0,-0.5],[47.5,-0.5]]},"holes":[],"area":3.0}]},{"body":"Case wall","z0":8.0,"z1":9.0,"regions":[{"outer":{"p":[[61.0,-2.5],[87.5,-2.5],[87.5,21.5],[110.0,21.5],[111.8238,25.7099],[85.7706,53.5],[98.0,53.5],[100.0,57.5],[79.0,85.5],[88.0,85.5],[89.9085,89.6148],[61.2705,123.46],[48.7295,123.46],[20.0915,89.6148],[22.0,85.5],[31.0,85.5],[10.0,57.5],[12.0,53.5],[24.2294,53.5],[-1.8238,25.7099],[0.0,21.5],[22.5,21.5],[22.5,-2.5],[29.0,-2.5],[29.0,-0.5],[24.5,-0.5],[24.5,23.5],[0.0,23.5],[-0.3648,24.342],[28.8459,55.5],[12.0,55.5],[11.6,56.3],[35.0,87.5],[22.0,87.5],[21.6183,88.323],[49.6571,121.46],[60.3429,121.46],[88.3817,88.323],[88.0,87.5],[75.0,87.5],[98.4,56.3],[98.0,55.5],[81.1541,55.5],[110.3648,24.342],[110.0,23.5],[85.5,23.5],[85.5,-0.5],[61.0,-0.5]]},"holes":[],"area":876.223},{"outer":{"p":[[42.0,-2.5],[49.0,-2.5],[49.0,-0.5],[42.0,-0.5]]},"holes":[],"area":14.0}]},{"body":"Case wall","z0":9.0,"z1":13.0,"regions":[{"outer":{"p":[[81.0,-2.5],[87.5,-2.5],[87.5,21.5],[110.0,21.5],[111.8238,25.7099],[85.7706,53.5],[98.0,53.5],[100.0,57.5],[79.0,85.5],[88.0,85.5],[89.9085,89.6148],[61.2705,123.46],[48.7295,123.46],[20.0915,89.6148],[22.0,85.5],[31.0,85.5],[10.0,57.5],[12.0,53.5],[24.2294,53.5],[-1.8238,25.7099],[0.0,21.5],[22.5,21.5],[22.5,-2.5],[29.0,-2.5],[29.0,-0.5],[24.5,-0.5],[24.5,23.5],[0.0,23.5],[-0.3648,24.342],[28.8459,55.5],[12.0,55.5],[11.6,56.3],[35.0,87.5],[22.0,87.5],[21.6183,88.323],[49.6571,121.46],[60.3429,121.46],[88.3817,88.323],[88.0,87.5],[75.0,87.5],[98.4,56.3],[98.0,55.5],[81.1541,55.5],[110.3648,24.342],[110.0,23.5],[85.5,23.5],[85.5,-0.5],[81.0,-0.5]]},"holes":[],"area":836.223},{"outer":{"p":[[42.0,-2.5],[49.0,-2.5],[49.0,-0.5],[42.0,-0.5]]},"holes":[],"area":14.0},{"outer":{"p":[[61.0,-2.5],[70.0,-2.5],[70.0,-0.5],[61.0,-0.5]]},"holes":[],"area":18.0}]},{"body":"Case wall","z0":13.0,"z1":15.6,"regions":[{"outer":{"p":[[81.0,-2.5],[87.5,-2.5],[87.5,21.5],[110.0,21.5],[111.8238,25.7099],[85.7706,53.5],[98.0,53.5],[100.0,57.5],[79.0,85.5],[88.0,85.5],[89.9085,89.6148],[61.2705,123.46],[48.7295,123.46],[20.0915,89.6148],[22.0,85.5],[31.0,85.5],[10.0,57.5],[12.0,53.5],[24.2294,53.5],[-1.8238,25.7099],[0.0,21.5],[22.5,21.5],[22.5,-2.5],[70.0,-2.5],[70.0,-0.5],[24.5,-0.5],[24.5,23.5],[0.0,23.5],[-0.3648,24.342],[28.8459,55.5],[12.0,55.5],[11.6,56.3],[35.0,87.5],[22.0,87.5],[21.6183,88.323],[49.6571,121.46],[60.3429,121.46],[88.3817,88.323],[88.0,87.5],[75.0,87.5],[98.4,56.3],[98.0,55.5],[81.1541,55.5],[110.3648,24.342],[110.0,23.5],[85.5,23.5],[85.5,-0.5],[81.0,-0.5]]},"holes":[],"area":918.223}]},{"body":"Standoff 1","z0":2.0,"z1":14.0,"regions":[{"outer":{"c":[22.5,29.0,3.25]},"holes":[{"c":[22.5,29.0,1.25]}],"area":28.117}]},{"body":"Standoff 2","z0":2.0,"z1":14.0,"regions":[{"outer":{"c":[88.0,29.0,3.25]},"holes":[{"c":[88.0,29.0,1.25]}],"area":28.117}]},{"body":"Standoff 3","z0":2.0,"z1":14.0,"regions":[{"outer":{"c":[48.0,111.5,3.25]},"holes":[{"c":[48.0,111.5,1.25]}],"area":28.117}]},{"body":"Standoff 4","z0":2.0,"z1":14.0,"regions":[{"outer":{"c":[62.0,111.5,3.25]},"holes":[{"c":[62.0,111.5,1.25]}],"area":28.117}]}],"stand":[{"body":"Stand","z0":-36.0,"z1":-6.0,"regions":[{"outer":{"p":[[-5.0,-50.0],[115.0,-50.0],[115.0,6.0],[-5.0,6.0]]},"holes":[{"p":[[15.0,-47.0],[15.0,-27.0],[95.0,-27.0],[95.0,-47.0]]},{"p":[[24.0,-24.0],[24.0,-3.0],[86.0,-3.0],[86.0,-24.0]]}],"area":3818.0}]},{"body":"Stand","z0":-6.0,"z1":-0.5,"regions":[{"outer":{"p":[[-5.0,-50.0],[115.0,-50.0],[115.0,6.0],[-5.0,6.0]]},"holes":[{"p":[[24.0,-24.0],[24.0,-3.0],[86.0,-3.0],[86.0,-24.0]]}],"area":5418.0}]},{"body":"Stand","z0":-0.5,"z1":16.1,"regions":[{"outer":{"p":[[-5.0,-50.0],[115.0,-50.0],[115.0,6.0],[88.0,6.0],[88.0,-3.0],[86.0,-3.0],[86.0,-24.0],[24.0,-24.0],[24.0,-3.0],[22.0,-3.0],[22.0,6.0],[-5.0,6.0]]},"holes":[],"area":4824.0}]},{"body":"Stand","z0":16.1,"z1":24.0,"regions":[{"outer":{"p":[[-5.0,-50.0],[115.0,-50.0],[115.0,6.0],[-5.0,6.0]]},"holes":[],"area":6720.0}]}]}


def plane_at(comp, z_mm):
    if abs(z_mm) < 1e-9:
        return comp.xYConstructionPlane
    pin = comp.constructionPlanes.createInput()
    pin.setByOffset(comp.xYConstructionPlane, adsk.core.ValueInput.createByReal(z_mm / 10.0))
    pl = comp.constructionPlanes.add(pin)
    pl.isLightBulbOn = False
    return pl


def draw_loop(sk, lp):
    if 'c' in lp:
        cx, cy, r = lp['c']
        sk.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(cx / 10.0, cy / 10.0, 0), r / 10.0)
        return
    pts = [adsk.core.Point3D.create(x / 10.0, y / 10.0, 0) for x, y in lp['p']]
    lines = sk.sketchCurves.sketchLines
    first = lines.addByTwoPoints(pts[0], pts[1])
    prev = first
    for p in pts[2:]:
        prev = lines.addByTwoPoints(prev.endSketchPoint, p)
    lines.addByTwoPoints(prev.endSketchPoint, first.startSketchPoint)


def build_part(root, name, slabs, color=None):
    occ = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    comp = occ.component
    comp.name = name
    bodies = []
    for i, s in enumerate(slabs):
        sk = comp.sketches.add(plane_at(comp, s['z0']))
        sk.name = '%s z%.1f' % (s['body'], s['z0'])
        sk.isComputeDeferred = True
        for reg in s['regions']:
            draw_loop(sk, reg['outer'])
            for h in reg['holes']:
                draw_loop(sk, h)
        sk.isComputeDeferred = False
        profs = [sk.profiles.item(k) for k in range(sk.profiles.count)]
        areas = [p.areaProperties(adsk.fusion.CalculationAccuracy.MediumCalculationAccuracy).area * 100.0 for p in profs]
        used = set()
        for reg in s['regions']:
            best, bi = None, None
            for k, a in enumerate(areas):
                if k in used:
                    continue
                d = abs(a - reg['area'])
                if best is None or d < best:
                    best, bi = d, k
            used.add(bi)
            ext_in = comp.features.extrudeFeatures.createInput(
                profs[bi], adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            ext_in.setDistanceExtent(False, adsk.core.ValueInput.createByReal((s['z1'] - s['z0']) / 10.0))
            ext = comp.features.extrudeFeatures.add(ext_in)
            for b in range(ext.bodies.count):
                bodies.append(ext.bodies.item(b))
    # join everything into one solid body
    if len(bodies) > 1:
        tools = adsk.core.ObjectCollection.create()
        for b in bodies[1:]:
            tools.add(b)
        ci = comp.features.combineFeatures.createInput(bodies[0], tools)
        ci.operation = adsk.fusion.FeatureOperations.JoinFeatureOperation
        ci.isKeepToolBodies = False
        comp.features.combineFeatures.add(ci)
    if comp.bRepBodies.count:
        comp.bRepBodies.item(0).name = name
    return occ


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = adsk.fusion.Design.cast(app.activeProduct)
        design.designType = adsk.fusion.DesignTypes.ParametricDesignType
        design.fusionUnitsManager.distanceDisplayUnits = adsk.fusion.DistanceUnits.MillimeterDistanceUnits
        root = design.rootComponent
        root.name = 'SydorenkoG12'
        build_part(root, 'Korpus', DATA['case'])
        build_part(root, 'Pidstavka', DATA['stand'])
        # PCB 3D model (optional)
        try:
            here = os.path.dirname(os.path.realpath(__file__))
            step = os.path.join(here, '..', '..', 'SydorenkoG12_PCBA.step')
            if os.path.exists(step):
                im = app.importManager
                im.importToTarget(im.createSTEPImportOptions(step), root)
        except:
            pass
        app.activeViewport.fit()
        ui.messageBox('SydorenkoG12: case and stand created.\nSave the design (File > Save) to get the .f3d project,\n'
                      'export bodies "Korpus" and "Pidstavka" as STL/3MF for printing.')
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
