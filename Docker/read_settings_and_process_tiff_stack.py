import sys

from java.io import File
from java.lang import System

from ij import IJ

from fiji.plugin.trackmate import TrackMate
from fiji.plugin.trackmate import Logger
from fiji.plugin.trackmate.io import TmXmlReader, TmXmlWriter


# We have to do the following to avoid errors with UTF8 chars generated in
# TrackMate that will mess with our Fiji Jython.
reload(sys)
sys.setdefaultencoding("utf-8")


print("reading data")
imp = IJ.openImage("https://fiji.sc/samples/FakeTracks.tif")
# imp = IJ.openImage("/data/segmented.tiff")
print("data read successfully")

print("Reading settings")
file = File("/data/settings.xml")
reader = TmXmlReader(file)
if not reader.isReadingOk():
    sys.exit(reader.getErrorMessage())
print("Settings read successfully")

model = reader.getModel()
model.setLogger(Logger.IJ_LOGGER)

settings = reader.readSettings(imp)

# -------------------
# Instantiate plugin
# -------------------

trackmate = TrackMate(model, settings)

# --------
# Process
# --------

ok = trackmate.checkInput()
if not ok:
    sys.exit(str(trackmate.getErrorMessage()))

ok = trackmate.process()
if not ok:
    sys.exit(str(trackmate.getErrorMessage()))

model.getLogger().log(str(model))

# --------
# Write output
# --------
f = File("/data/results.xml")
xml_writer = TmXmlWriter(f)

xml_writer.appendModel(model)
xml_writer.appendSettings(settings)
xml_writer.writeToFile()

System.exit(0)
