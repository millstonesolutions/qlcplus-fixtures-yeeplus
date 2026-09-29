N=30
L5=[20,38,71,133,255]
def bg():
    BG=[(0,0,0)]+[(v,0,0) for v in L5]+[(0,v,0) for v in L5]+[(0,0,v) for v in L5]+[(v,v,0) for v in L5]+[(v,0,v) for v in L5]+[(0,v,v) for v in L5]+[(v,v,v) for v in L5]
    for i,(r,g,b) in enumerate(BG):
        lo=7*i; hi=255 if i==len(BG)-1 else 7*i+6
        name="Off (black)" if i==0 else f"R{r} G{g} B{b}"
        a(f'  <Capability Min="{lo}" Max="{hi}" Preset="ColorMacro" Res1="#{r:02x}{g:02x}{b:02x}">{name}</Capability>')
L=[]; a=L.append
a('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE FixtureDefinition>\n<FixtureDefinition xmlns="http://www.qlcplus.org/FixtureDefinition">')
a(' <Creator>\n  <Name>Q Light Controller Plus</Name>\n  <Version>4.14.4</Version>\n  <Author>Heath</Author>\n </Creator>')
a(' <Manufacturer>YeeSite</Manufacturer>\n <Model>60W RGB Pixel Light Bar</Model>\n <Type>LED Bar (Pixels)</Type>')
for c in ("Red","Green","Blue"): a(f' <Channel Name="{c}" Preset="Intensity{c}"/>')
a(' <Channel Name="Master dimmer" Preset="IntensityMasterDimmer"/>')
a(' <Channel Name="Strobe">\n  <Group Byte="0">Shutter</Group>\n  <Capability Min="0" Max="9" Preset="ShutterOpen">Strobe off</Capability>\n  <Capability Min="10" Max="255" Preset="StrobeSlowToFast">Strobe slow to fast</Capability>\n </Channel>')
a(' <Channel Name="Built-in Program">\n  <Group Byte="0">Effect</Group>\n  <Capability Min="0" Max="2">Off</Capability>')
for i in range(67):
    what="colour from RGB channels" if i<47 else "preset colour"
    a(f'  <Capability Min="{3+3*i}" Max="{5+3*i}">Program {i+1} ({what})</Capability>')
a('  <Capability Min="204" Max="206">Program 68 (cycle through programs 1-67)</Capability>')
for k,(lo,hi) in enumerate([(207,209),(210,212),(213,255)]):
    a(f'  <Capability Min="{lo}" Max="{hi}">Sound {k+1} (colour from RGB channels)</Capability>')
a(' </Channel>')
a(' <Channel Name="Program Speed">\n  <Group Byte="0">Speed</Group>\n  <Capability Min="0" Max="255">Program speed slow to fast</Capability>\n </Channel>')
a(' <Channel Name="Program Background Colour">\n  <Group Byte="0">Colour</Group>')
bg()
a(' </Channel>')
for p in range(1,N+1):
    for c in ("Red","Green","Blue"): a(f' <Channel Name="{c} {p}" Preset="Intensity{c}"/>')
def mode(name,chs,heads=False):
    a(f' <Mode Name="{name}">')
    for i,c in enumerate(chs): a(f'  <Channel Number="{i}">{c}</Channel>')
    if heads:
        for p in range(N):
            a('  <Head>'); [a(f'   <Channel>{3*p+k}</Channel>') for k in range(3)]; a('  </Head>')
    a(' </Mode>')
pix=[f"{c} {p}" for p in range(1,N+1) for c in ("Red","Green","Blue")]
prog=["Built-in Program","Program Speed","Program Background Colour"]
mode("3 Channel",["Red","Green","Blue"])
mode("5 Channel",["Master dimmer","Strobe","Red","Green","Blue"])
mode("8 Channel",["Master dimmer","Strobe","Red","Green","Blue"]+prog)
mode("90 Channel",pix,True)
mode("94 Channel",pix+["Strobe"]+prog,True)
a(' <Physical>\n  <Bulb Type="LED" Lumens="0" ColourTemperature="0"/>\n  <Dimensions Weight="0" Width="1000" Height="0" Depth="0"/>\n  <Lens Name="Other" DegreesMin="90" DegreesMax="90"/>\n  <Focus Type="Fixed" PanMax="0" TiltMax="0"/>')
a(f'  <Layout Width="{N}" Height="1"/>\n  <Technical PowerConsumption="60" DmxConnector="3-pin"/>\n </Physical>\n</FixtureDefinition>')
open(__import__('os').path.join(__import__('os').path.dirname(__file__),'YeeSite','YeeSite-60W-RGB-Pixel-Light-Bar.qxf'),'w').write("\n".join(L)+"\n")
