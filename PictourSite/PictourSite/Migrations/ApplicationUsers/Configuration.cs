namespace PictourSite.Migrations.ApplicationUsers
{
    using Microsoft.AspNet.Identity;
    using Microsoft.AspNet.Identity.EntityFramework;
    using Models;
    using System;
    using System.Data.Entity;
    using System.Data.Entity.Migrations;
    using System.Linq;

    internal sealed class Configuration : DbMigrationsConfiguration<PictourSite.Models.ApplicationDbContext>
    {
        public Configuration()
        {
            AutomaticMigrationsEnabled = false;
            MigrationsDirectory = @"Migrations\ApplicationUsers";
        }

        protected override void Seed(PictourSite.Models.ApplicationDbContext context)
        {
            var manager =
                 new UserManager<ApplicationUser>(
                     new UserStore<ApplicationUser>(context));

            var roleManager =
                new RoleManager<IdentityRole>(
                    new RoleStore<IdentityRole>(context));

            roleManager.Create(new IdentityRole { Name = "Admin" });
            roleManager.Create(new IdentityRole { Name = "User" });

            context.Users.AddOrUpdate(u => u.Email, new ApplicationUser
            {
                UserName = "einstine.albert@itsligo.ie",
                Email = "einstine.albert@itsligo.ie",
                EmailConfirmed = true,
                PasswordHash = new PasswordHasher().HashPassword("ITSligo$1"),
                SecurityStamp = Guid.NewGuid().ToString(),
            });

            context.Users.AddOrUpdate(u => u.Email, new ApplicationUser
            {
                UserName = "blogs.joe@itsligo.ie",
                Email = "blogs.joe@itsligo.ie",
                EmailConfirmed = true,
                PasswordHash = new PasswordHasher().HashPassword("ITSligo$2"),
                SecurityStamp = Guid.NewGuid().ToString(),
            });

            context.SaveChanges();

            ApplicationUser Admin = manager.FindByEmail("einstine.albert@itsligo.ie");
            if (Admin != null)
            {
                manager.AddToRoles(Admin.Id, new string[] { "Admin", "User" });
            }
            else
            {
                throw new Exception { Source = "Did not find user" };
            }

            ApplicationUser User = manager.FindByEmail("blogs.joe@itsligo.ie");
            if (User != null)
            {
                manager.AddToRoles(User.Id, new string[] { "User" });
            }
            else
            {
                throw new Exception { Source = "Did not find user" };
            }
        }
    }
}
