using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using ProxyBypassifier.Snatcher;

namespace ProxyBypassifier.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        public ContentResult Get()
        {
            var result = new ContentResult();
            result.Content = WebSnatcher.Get(@"http://msdn.com");
            result.ContentEncoding = System.Text.Encoding.UTF8;
            result.ContentType = @"text/html";
            return result;
        }
    }
}
