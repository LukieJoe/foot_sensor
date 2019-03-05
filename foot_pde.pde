import processing.serial.*;

// for accelerameter
float xmag = 0, ymag = 0;
float newXmag, newYmag = 0; 

Serial my_port;

String input;
String[] data, p, a;
FloatList pads, accel;

// pads -> mf, mm, hl, lf
// accel -> 

final int xval=320, yval=330;

void setup() { 
  size(640, 640, P3D); 
  //noStroke();
  noLoop();
  colorMode(RGB, 1);
  smooth();
  
  my_port = new Serial(this, "/dev/rfcomm0", 9600);
  
  pads = new FloatList();
  accel = new FloatList();
  
  for(int i=0; i<4; ++i)
    pads.append(0);
  
  // Y,X
  accel.append(yval);
  accel.append(xval);
} 

void draw() { 
  background(0.5);
  scale(1.2,1.2,1.2);
  
  //println( pads.get(0), pads.get(1), pads.get(2), pads.get(3) );
  //println( accel.get(0), accel.get(1) );
  // TODO DRAW TEXT TOP LEFT ( GRAPH? )

  // Y:330 -> roll -> get(0) -> left:=bigger
  // X:320 -> pitch -> get(1) -> forward:=bigger
  ymag = radians( 330 - accel.get(0) );
  xmag = radians( 320 - accel.get(1) );
  
  pushMatrix();
  fill(0.5);
  //noFill();
  translate( 200 , 300, -30); // center of screen

  rotateX( -xmag ); 
  rotateY(  ymag );
  
  // TODO DEFINE SHAPE OBJ ONCE
  beginShape();

  curveVertex(25, 20, -1);
  
  curveVertex(10, -40, -1);
  curveVertex(30, -80, -1);
  
  curveVertex(60, -80, -1);
  curveVertex(80, -40, -1);
  
  curveVertex(80, 20, -1);
  curveVertex(80, 75, -1);
  
  curveVertex(65, 110, -1);
  curveVertex(45, 110, -1);
  
  curveVertex(25, 75, -1);
  curveVertex(25, 20, -1);
  
  curveVertex(10, -40, -1);
  curveVertex(30, -80, -1);

  endShape();
  
  ellipseMode( CENTER );
  
  translate(42, -65);
  
  fill(204, 102, 0);
  ellipse( 0,0, pads.get(0), pads.get(0) );
  
  translate(20, 25);
  
  fill(204, 102, 0);
  ellipse( 0,0, pads.get(3), pads.get(3) );
  
  translate(-30, 20);
  
  fill(204, 102, 0);
  ellipse( 0,0, pads.get(1), pads.get(1) );
  
  translate(20, 110);
  
  fill(204, 102, 0);
  ellipse( 0,0, pads.get(2), pads.get(2) );
  
  popMatrix();

}

void serialEvent (Serial my_port) {
  try{
    if (my_port.available() > 0){
      input = my_port.readStringUntil('\n');
      if (input != null) {
        data = split(input, ';');
        
        p = split(data[0], ',');
        a = split(data[2], ',');
        
        // loop through 4 pressure points <data[0]>
        for(int i=0; i<p.length; i++){
          if (!Float.isNaN(float(p[i])))
            pads.set( i,map(float(p[i]), 0, 1023, 0, 35) );
          else
            pads.set( i,30 );
        }
        
        for(int i=0; i<a.length; i++){
          if (!Float.isNaN(float(a[i])))
            ;// accel.set( i,float(a[i]) );
          else
            ;// accel.set( i,1024 );
        }
        
        //if (!Float.isNaN(float(data[0])))
        //  pads.append(map(float(data[0]), 0, 1023, 0, height));
        //print("INPUT: ");
        
        // ACCEL DATA
        // StringList accel_data = new StringList(a);
        // println( accel_data );
        
        //TODO post processing
        // Step length -- while pressure in pads
        // Stride length -- while no pressure in pads
        // Cadence -- ( # steps / min )
        // Speed -- distance covered over time
        // Step Count -- inc # steps
        
        //GATHER USE DATA
        // Normal Gait(walking straight, feet parallel)
        // In-toeing
        // Out-toeing
        // Tiptoeing
        // Walking on the heel
        
        // Stance Phase := foot flat with ground
        // Calculate for each stride
        // MFP ( ( MM + MF ) * 100 ) / ( MM + MF + LF + H + 0.001 )
        
        // Active time -- from accel
        
        redraw(); // draw only when updated
        //accel.clear(); pads.clear(); // empty the FloatList
      }
    }
  }
  catch (Exception e){ // avoid crashing if serial read is not present or fails
    println("Serial Exception Intercepted");
    //e.printStackTrace();
  }
}
