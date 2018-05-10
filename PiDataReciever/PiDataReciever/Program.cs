using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace PiDataReciever
{
    class Program
    {
        static void Main(string[] args)
        {

            //Creates a UdpClient for reading incoming data.
            UdpClient udpServer = new UdpClient(7777);

            //Creates an IPEndPoint to record the IP Address and port number of the sender.  
            IPAddress ip = IPAddress.Parse("192.168.3.209");
            IPEndPoint RemoteIpEndPoint = new IPEndPoint(ip, 7777);

            try
            {
                // Blocks until a message is received on this socket from a remote host (a client).
                Console.WriteLine("Server is blocked");
                while (true)
                {
                    Console.WriteLine("Recieving data from Raspberry Pi");
                    Byte[] receiveBytes = udpServer.Receive(ref RemoteIpEndPoint); // modtager bytes
                    string receivedData = Encoding.ASCII.GetString(receiveBytes);  // laver bytes til string 
                    Console.WriteLine("Data is transferred");

                    string[] array = receivedData.Split(' ');
                    string test = array[0];
                    Console.WriteLine(test);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }
    }
}
