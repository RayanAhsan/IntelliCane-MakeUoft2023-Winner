const int trigPin = 9;
const int echoPin = 10;
// defines variables
long duration;
int distance;
int buzzerPin = 12; 
void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600); // Starts the serial communication
  pinMode(buzzerPin, OUTPUT);
}
void loop() {
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);



  // Calculating the distance
  distance = duration * 0.034 / 2;

    if (distance == 0){
    distance = 250;
  }
  // Prints the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.println(distance);
  int button_state = digitalRead(buzzerPin);

  if (distance < 65) {
    digitalWrite(buzzerPin, HIGH);

  } else if (distance > 65){
    digitalWrite(buzzerPin, LOW);
  }

}