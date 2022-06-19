
#include <SPI.h>
#include <Ethernet.h>

byte mac[] = { 0x78, 0xAC, 0xC0, 0x63, 0xBA, 0x62 };

IPAddress server(192,168,1,1);  

IPAddress ip(192, 168, 1, 2);
IPAddress myDns(192, 168, 0, 1);

EthernetClient client;


unsigned long beginMicros, endMicros;
unsigned long byteCount = 0;
bool printWebData = true;  // set to false for better speed measurement

void setup(){
      Serial.begin(9600);
      while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
        pinMode(2,OUTPUT);
        pinMode(3,OUTPUT);
        pinMode(3,OUTPUT);
        pinMode(4,OUTPUT);
        pinMode(5,OUTPUT);
        pinMode(6,OUTPUT);
        pinMode(7,OUTPUT);
        pinMode(8,OUTPUT);
        pinMode(9,OUTPUT);
        pinMode(10,OUTPUT);
        pinMode(11,OUTPUT);
        pinMode(12,OUTPUT);
        pinMode(13,OUTPUT);    
      }
    

  void loop() {

    while (true){
       int pre;
       pre = 0;               

      Serial.println("Initialize Ethernet with DHCP:");

      Ethernet.begin(mac, ip, myDns);
      delay(1000);
      Serial.print("connecting to ");
      Serial.print(server);
      Serial.println("...");

      if (client.connect(server, 10000)) {
        Serial.print("connected to ");
        Serial.println(client.remoteIP());
        while (pre < 1){
          //delay (1);
          int pin2 = digitalRead(2);
          int pin3 = digitalRead(3);
          int pin4 = digitalRead(4);
          int pin5 = digitalRead(5);
          int pin6 = digitalRead(6);
          int pin7 = digitalRead(7);
          int pin8 = digitalRead(8);
          int pin9 = digitalRead(9);
          int pin10 = digitalRead(10);
          int pin12 = digitalRead(12);
          int pin13 = digitalRead(13);
          int pina0 = analogRead(A0);
          int pina1 = analogRead(A1);
          int pina2 = analogRead(A2);
          int pina3 = analogRead(A3);
          int pina4 = analogRead(A4);
          int pina5 = analogRead(A5);
          analogWrite(11,pina0);
          int pinp11 = analogRead(11);
          String p2 = String (pin2);
          String p3 = String (pin3); 
          String p4 = String (pin4); 
          String p5 = String (pin5); 
          String p6 = String (pin6); 
          String p7 = String (pin7);
          String p8 = String (pin8);
          String p9 = String (pin9);
          String p10 = String (pin10);
          String p12 = String (pin12);
          String p13 = String (pin13); 
          String pa0 = String (pina0); 
          String pa1 = String (pina1);
          String pa2 = String (pina2);
          String pa3 = String (pina3);
          String pa4 = String (pina4);
          String pa5 = String (pina5);
          String pwn11 = String (pinp11);
          String per = p2+p3+p4+p5+p6+p7+p8+p9+p10+"0"+p12+p13+pa0+pa1+pa2+pa3+pa4+pa5+"000"+"000"+"000"+"000"+"000"+pwn11+"uno"+"1"+"1"+"1"+"1"+"1"+"1"+"1"+"2"+"2"+"3"+"2"+"2";  
          client.print(per);
          if (client.available()) {
            String ser = client.readString();
            Serial.println(ser);
            if (char(ser[2]) == '1') digitalWrite(2,HIGH);
            if (char(ser[2]) == '0') digitalWrite(2,LOW);
            if (char(ser[7]) == '1') digitalWrite(3,HIGH);
            if (char(ser[7]) == '0') digitalWrite(3,LOW);
            if (char(ser[12]) == '1') digitalWrite(4,HIGH);
            if (char(ser[12]) == '0') digitalWrite(4,LOW);
            if (char(ser[17]) == '1') digitalWrite(5,HIGH);
            if (char(ser[17]) == '0') digitalWrite(5,LOW);
            if (char(ser[22]) == '1') digitalWrite(6,HIGH);
            if (char(ser[22]) == '0') digitalWrite(6,LOW);
            if (char(ser[27]) == '1') digitalWrite(7,HIGH);
            if (char(ser[27]) == '0') digitalWrite(7,LOW);
            if (char(ser[32]) == '1') digitalWrite(8,HIGH);
            if (char(ser[32]) == '0') digitalWrite(8,LOW);
            if (char(ser[37]) == '1') digitalWrite(9,HIGH);
            if (char(ser[37]) == '0') digitalWrite(9,LOW);
            if (char(ser[42]) == '1') digitalWrite(10,HIGH);
            if (char(ser[42]) == '0') digitalWrite(10,LOW);
            if (char(ser[47]) == '1') digitalWrite(11,HIGH);
            if (char(ser[47]) == '0') digitalWrite(11,LOW);
            if (char(ser[52]) == '1') digitalWrite(12,HIGH);
            if (char(ser[52]) == '0') digitalWrite(12,LOW);
            if (char(ser[57]) == '1') digitalWrite(13,HIGH);
            if (char(ser[57]) == '0') digitalWrite(13,LOW);
            if (!client.connected()) {
              Serial.println ("Disconnect");
              break;
            
            }
            }
          }
          }
        }
      }
