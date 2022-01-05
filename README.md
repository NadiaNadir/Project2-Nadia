# Project - 2.
## Team Members: Nadia Nadir & Paulo Corzo. 
# An Automated Trading bot that uses websockets, TA-Lib, and the Binance 
#### It will retrieve real-time price data & we apply technical  indicators to this Price Data in order to execute trades automatically 
![A](https://user-images.githubusercontent.com/60047689/148145549-3cbfdf4b-1443-4c61-8af4-c6e0681a427b.jpeg)

#
### Project Explaination. 

#### THE MECHANISM WE ARE USING FOR TRADING BOT. (DIAGRAM)
![DataFloeDiagram](https://user-images.githubusercontent.com/60047689/147998538-fc8c3c2c-7323-4cb0-ae3d-8137207008e0.png)
  
  Bianance is going to be our BROKER. So we are going to execute ORDERS through the BINANCE API. 
BIANANCE is also going to be our DATA PROVIDER. 
Our Data Provider & Our Broker are not always the same thing. Like in this Case we can get the DATA from Bianance & there is a variety of ways we can get the data from the Binance like we can use rest API to pull the data from biannace. 
For this project we use WEBSOCKET  
So the way WEBSOCKET work… um .. Websocket Binance Provides a Bunch of Stream, so there’s a STREAMING DATA COMING and those Streams all have different names. 
And what we do is… we have a Client Connect to one of those Websocket Streams and maintain a PERSISTENT CONNECTION rather than Always Requesting Data with a http request. 
So the Binance is Providing the Streams of Data like on of the Steam of data is the Bitcoin Prices like BTCUSDT… and Ethereum & litecoin and other Bunch of CryptoCurrencies. 
So these streams are always beign PUSH OUT at all times and so this DATA is being PUBLISHED 
And on these Streams we have streams of the Price Data so we will get OPEN HIGH LOW ENCLOSED DATA, CANDLE STICKS & also INDIVIDUAL TICKS … that make up those Candlesticks.. 
so we get the Price for Ethereum for instance of you know 3756.99 3756.88 3756.79 and so forth. 
So there is BUNCH OF PRICES Coming in… and as NEW ORDERS COMES IN there prices FLUCTUATE UP & DOWN. 
SO I have all the Streams of Data.. .so now I need to PROVIDE SOME TYPE OF CLIENT TO CONNECT & READ this data from this WEBSOCKET SERVER. 
So I am going to use the PYTHON WEBSOCKET CLIENT. 
This is going to be READING DATA from these STREAMS. 
So this DATA is ALWAYS being Provided and I just needed these Clients to walk up to this Data take this data from the stream. 
Then our PYTHON CLIENT here…  we are going read in this DATA  or get some DATA coming in.. 
WE are Interested in just the CLOSING PRICES so it might be 1, 2, 3 … so on.  
We used TA-LIB to apply the RSI INDICATOR. RSI is Relative Strength Index. 
And we also apply any of our CANDLESTICK PATTERN. 
So we apply the RSI INDICATOR to this SERIES of DATA and then based on the Value of that it is going to give us the Value like 42.32 and so forth. 
If that number is GREATER THAN 70 … we are going to Hit BINANCE as a BROKER here. And they give us the API for Buying & Selling. (it will send http reuest to Binance)
If its LESS THAN 30 that means the STOCK IS OVERSOLD. And we are going to issue a BUY. 
And that’s the BASIC MECHANICS of what we BUILT.
We can add difference logics here to use any indicator we want, any patterns or whatever we want to fill in this code. 
So here is just showing the General Flow of Data … we apply the strategy of that data and than issuing BUYS & SELL ORDERS. 
  
    
#### REQUIREMENT.TXT FILE  

     ![C](https://user-images.githubusercontent.com/60047689/148145834-9106f07a-b369-4eed-a0a7-bc2443048eaf.png)

     For this Bot you need to Install the WEBSOCKET and TA-LIB to Process this Price DATA. 
1)	So we need the PYTHON-BINANCE CLIENT. You can find it inside the the BINANCE DOCUMNETATION on Github. 
2)	Then we will need TA-LIB ( as I explained in my diagram) 
3)	Then we need NUMPY – which is use for Calculation on NUMOY ARRAYS so it provides a way to PERFORM a really Efficient Optimal Calculations on series of numbers. 
4)	We also need a WEBSOCKET CLIENT for Python. 

I created a Separate requirement.txt file then I just run this pip3 install –r requirements.txt in my terminal. It will install all the packages we required. 

# CONFIG.PY 
There is a file CONFIG.PY where you need to add your Binance API Key & Binance Secret Key. 
### LET”S CHECKOUT THE CODE FILE

![D](https://user-images.githubusercontent.com/60047689/148145899-1a10e147-5f02-4d7a-b6a9-cbc51d8e7b6e.png)

First we import the WEBSOCKET which is the Part of the WEBSOCKET CLIENT PACKAGE. 
![E](https://user-images.githubusercontent.com/60047689/148145979-6e404842-5bb3-4a0b-a598-19b649b28792.png)

and then
![F](https://user-images.githubusercontent.com/60047689/148146053-c9bd525c-73c5-4793-ab71-beec83a06fe1.png)

#### SOCKET = Variable for Websocket. 
streamname: https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#general-wss-information
 I Add Symbol for ETH "ethusd", it provides process for Ethereum.
then Adding kline then an interval of 1 minute. (you can change it) 

and then... 
##### WE CREATE WEBSOCKET CLIENT 

![G](https://user-images.githubusercontent.com/60047689/148146133-fa30b1ae-d02a-4955-8cc6-c95a68d04ed3.png)

we Create a New Websocket Client - check the Bianance Documentation for differenct stream names. Check out the link and the images: 
https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#klinecandlestick-streams

![binance-klinestick-A](https://user-images.githubusercontent.com/60047689/148146203-f76b4aa8-7341-46c5-851f-86b3396b268a.png)

![binance-klinestick-B](https://user-images.githubusercontent.com/60047689/148146212-3b6c6b0d-e868-4b2c-8c98-0453eced5b74.png)

The base endpoint is: wss://stream.binance.com:9443 (this is all the data stream from)
then we will need callback functions.
To connect it with SOCKET I need to define a Variety of Functions here. 
We need FUNCTIONS for OPEN an CONNECTTION, WE need CLOSE, and we also need ab ON-Message. 

#### Now adding FUNCTIONS INSIDE THE WEBSOLCET CLIENT: 
![H](https://user-images.githubusercontent.com/60047689/148146265-8c332764-2ea9-4481-a9d6-3bcba53531fb.png)
![i](https://user-images.githubusercontent.com/60047689/148146278-b06935fb-31fa-4807-8967-4d6dfbc76084.png)


#### DEPENDENCIES & 3rd PARTY LIBRARAIES WE WILL NEED. 
https://github.com/NadiaNadir/Project2-Nadia/blob/main/requirements.txt  
1 ) PYTHON-BINANCE  
2 ) TA-Lib (Technical Analysis Library)  
3) numpy (for calculations on numpy arrays, it provides a really efficient optimal calculations on series of numbers)  
4) WEBSOCKET CLIENT for Python.   
So we define these FUNCTIONS here. 
Define Function on-open. 
When the websocket os CLOSE … close count. 
And then ON-MESSAGE we can PRINT RECEIVED message. 
Like after we connect we receive all the different events when we are connected to the websocket.   
And we TELL PYTHON what FUNCTION to execute when these events happen. 

#### WS RUN FUNCTION
![J](https://user-images.githubusercontent.com/60047689/148146356-26a423f6-2546-46b6-909f-927fdfc7f55f.png)
We need this WS RUN FUCNTION and it’s called RUN FOREVER to run the WEBSOCKET APP. 

![K](https://user-images.githubusercontent.com/60047689/148146398-b1118366-b21e-4d52-bf14-5a4b9a267d92.png)

We use the ws for WEB SOCKETS because these Functions need a Refference to the WEBSOCKET. 
Because Each of these Functions received an INPUT of WS and the ON-MESSAGE will receive an activated message. 
On-message has the OPEN HIGH and LOW CLOSE DATA. 

Json-message = json.loads.  
Because we are reveiving the Json data.  
When X = true that measn NEW CANDLE STICK has started.

![M](https://user-images.githubusercontent.com/60047689/148146463-3888a66f-32f8-408e-a0dc-ad336ccf409d.png)
Here is the more detailed expalinton of what we are getting in the OUTPUT. 
So for me Closing Price is more important. 
So that’s why I use this code here: 
![N](https://user-images.githubusercontent.com/60047689/148146525-0b56b8e9-b963-4f72-b383-5652033e142b.png)

![L](https://user-images.githubusercontent.com/60047689/148146593-f6e91605-c7cd-455e-bf23-ea12070729e5.png)

Ok I also import pprint the Python Pretty Printing Functionality :D for easier format to read.
Now here we are getting the PRICE DATA for etherium. 
![image](https://user-images.githubusercontent.com/60047689/148146667-e6892ba5-02cf-4f2c-8461-df0dd2e61112.png)
When X = TRUE there than it’s the Final Value of the Candlesticks.. it’s the CLOSE of the Candlesticks.   

#### NOW WE WANT THE RSI INDICATOR. 
Which can process our data based on a series of closes. 
We wanted to actually track a series of closes.
CLOSES variable  
I create here a global variable and I call it Closes
![o](https://user-images.githubusercontent.com/60047689/148146779-a80f611e-86e3-4941-b256-e48147f59ab8.png)
And here I can get a Reference to that so I can do Global Closes 
![P](https://user-images.githubusercontent.com/60047689/148146808-22691558-f250-4a81-b7c5-16c1eab1e447.png)

For RSI WE used this formula. I got this from a book “Technical Ananlysis Explained” by Martin Pring. 
![RSI](https://user-images.githubusercontent.com/60047689/148146837-87841487-a549-4ad1-9c12-7d60b82f22c3.png)
You can calculate the RSI using etherium porice data that we are getting from these websockets. 
So now here we set up a contant for our RSI.
Like the RSI equals to 14. And these are the just default settings that people normally use. But we can adjust if we want it to be more overbought or more oversold. 
So these are our various Thresholds that we are going to use to determine weather to EXECUTE or BUY or SELL ORDER. 

![Q](https://user-images.githubusercontent.com/60047689/148146892-5a8f437e-a5a3-4f48-a36c-321d640772ab.png)

#### TRADE_SYMBOL = ETHUSDT. 
Becaue we are going to be trading Etherium here so it’s the Symbol from Binance. 
And then there is a QUANTITY we want toi buy. We can change it according to our BOTS BEHAVIOUR. 

#### RSI – TA LIB
So here we call the RSI function which is the PART of the TA LIB PACKAGE. 
And then we give it a default period. 
This will calculate the Series of RSI Values so once we get 15 closes we will get 1 RSI VALUE. 
But on the 16th Closewe will get the 2nd RSI Value so far. 
![R](https://user-images.githubusercontent.com/60047689/148146952-4c0ae2f5-8de2-4316-95e3-6b5795f594fe.png)

SO that’s how the WHOLE BOIT WORKS.
I spent 20 USDs, I gainged then i loose, but after like 2 days I earned profit of 0.33 :D 

##### __________
##### NOTE  
We have also upload a file name bots-notebook.ipynb   
We can use this file on sagemaker with it's noit working on the local directory. 
