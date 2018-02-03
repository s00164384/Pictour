using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(PictourSite.Startup))]
namespace PictourSite
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
