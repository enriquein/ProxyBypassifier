using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Net;


namespace ProxyBypassifier.Snatcher
{
    public class WebSnatcher
    {
        public static string Get(string url)
        {
            WebClient client = new WebClient();
            return client.DownloadString(url);
        }
    }
}