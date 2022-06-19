#include <ESP8266WiFi.h>
#include <SPI.h>

int status = WL_IDLE_STATUS;
IPAddress server(192,168,43,62); 


WiFiClient client;

unsigned long beginMicros, endMicros;
unsigned long byteCount = 0;
bool printWebData = true;

void setup() {
  Serial.begin(115200);
  Serial.println("! Инициализация !"); 
  pinMode(D2,INPUT);
  pinMode(D3,INPUT);
  pinMode(D3,INPUT);
  pinMode(D4,INPUT);
  pinMode(D5,INPUT);
  pinMode(D6,INPUT);
  pinMode(D7,INPUT);
  pinMode(D8,OUTPUT); 
  int pre;
  pre = 2; 
}


void loop() {
  WiFi.begin("BR2", "14881488");
  Serial.print("Подключаемся");   
    while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");}
  Serial.println();
  Serial.print("Подключен, IP address: ");
  Serial.println(WiFi.localIP());
  client.connect(server,10000);
  Serial.println("Подключаюсь к серверу.");
    while(true){
      delay(100);
      client.write("TEST");
  }
        
      
      
  }
