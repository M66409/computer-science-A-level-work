using System;
namespace testgame
{
    public class Player
    {
        public int max_health;
        public int health;
        public int health_pots;
        public int damage;
        public int defence;
        public int gold;
        public string armour;
        public string weapon;
        public Boolean alive;
        public int level;
        public int xp;
        public int xp_needed;
        public int health_pots_price;
        public int damage_increase;
        public int defence_increase;
        public int adamage;
        public int adefence;
        public Player()
        {
            Random random = new Random();
            max_health = 100;
            health = max_health;
            health_pots = random.Next(0, 5);
            damage = 5;
            defence = 0;
            gold = random.Next(10, 30);
            armour = "No Armour";
            weapon = "No Weapon";
            alive = false;
            level = 1;
            xp = 0;
            xp_needed = xp + (level * 50) + 100;
            health_pots_price = random.Next(10, 30);
            damage_increase = 0;
            defence_increase = 0;
            adamage = damage + damage_increase;
            adefence = defence + defence_increase;
        }

        public static void commands()
        {
            Console.WriteLine("use the inventory command for your inventory");
            Console.WriteLine("use the fight command to fight an enemy");
            Console.WriteLine("use the shop command to buy equipment from a shop");
            Console.WriteLine("use the heal command to use health potions");
        }



        public virtual void Fight(Player Player)
        {
            Random random = new Random();
            String[] enemy = ["skeleton", "zombie", "slime", "ghost", "goblin", "rat"];
            int[,] enemy_stats = { { random.Next(15, 45), random.Next(5, 15), random.Next(5, 10), random.Next(1, 5), random.Next(20, 40), random.Next(1, 3) },
            { 15, 10, 5, 1, 13, 2 },
            { random.Next(45, 135), random.Next(15, 45), random.Next(10, 30), random.Next(5, 15), random.Next(40, 120), random.Next(3, 9)},
            { random.Next(15, 25), random.Next(3, 7), random.Next(3, 5), random.Next(1, 5), random.Next(12, 22), random.Next(1, 3)}};
            int index = random.Next(0, 5);
            String current_enemy = enemy[index];
            int ehealth;
            int edamage;
            if (Player.level < 2)
            {
                ehealth = enemy_stats[0, index];
                edamage = enemy_stats[1, index];
            }
            else
            {
                ehealth = (int)Math.Round(enemy_stats[0, index] * Math.Sqrt(Player.level));
                edamage = (int)Math.Round(enemy_stats[1, index] * Math.Sqrt(Player.level));
            }
            int reward = enemy_stats[2, index];
            int xp_reward = enemy_stats[3, index];
            Console.WriteLine("A " + current_enemy + " has appeared");
            Console.WriteLine("The " + current_enemy + " has " + ehealth + " health and does " + edamage + " damage");
            while (ehealth > 0 || Player.health > 0)
            {
                int edamage_done = (int)(edamage - Math.Round(((double)Player.defence / 5)));
                if (edamage_done <= 0)
                {
                    Player.health -= 0;
                }
                else if (edamage_done > 0)
                {
                    Thread.Sleep(1500);
                    Console.WriteLine("You have " + Player.health + " health and the enemy has " + ehealth + " health");
                    Player.health -= edamage_done;
                    int damage_done = random.Next((Player.adamage - 5), (Player.adamage + 5));
                    if (damage_done <= 0)
                    {
                        ehealth -= 0;
                    }
                    else
                    {
                        ehealth -= damage_done;
                    }
                }
                if (Player.health <= 0)
                {
                    if (Player.health_pots > 1)
                    {
                        Player.heal(Player);
                        Console.WriteLine("You make one last stand against the " + current_enemy);
                    }
                    else
                    {
                        Console.WriteLine("You have died");
                        Player.alive = false;
                        break;
                    }
                }
                if (ehealth <= 0)
                {
                    Player.gold = Player.gold + reward;
                    Player.xp = Player.xp + xp_reward;
                    Thread.Sleep(1500);
                    Console.WriteLine("The " + current_enemy + " has been slain");
                    Console.WriteLine("You have gained "+ reward+" gold.You now have "+ Player.gold+ " gold");
                    Console.WriteLine("you gained "+ xp_reward+" xp.You now have "+ Player.xp+ " xp");
                    Console.WriteLine("your health is "+Player.health);
                    playing(Player);
                }
            }
        }
        public static void shop(Player Player)
        {
            String[] armour = ["leather armour", "bronze armour", "steel armour", "obsidian armour", "ancient armour"];
            int[,] armour_stats = { { 5, 10, 20, 25, 50 }, { 25, 30, 50, 60, 120 } };
            String[] weapons = ["rusty sword", "steel sword", "knife", "rusty knife", "gold sword"];
            int[,] weapon_stats = { { 8, 15, 11, 7, 20 }, { 25, 50, 35, 15, 65 } };
            Console.WriteLine("Would you like to see the armour,weapons or potions\n");
            String choice = Convert.ToString(Console.ReadLine())!;
            switch (choice.ToLower())
            {
                case "armour":
                    for (int i = 0; i <= armour.Length-1; i++)
                    {
                        Console.WriteLine(i + 1 + ":" + armour[i] + " Defense: " + armour_stats[0, i] + " Price: " + armour_stats[1,i] + " Gold\n");
                    }
                    Console.WriteLine("\nWhat armour set would you like to buy?\n");
                    int to_buy = Convert.ToInt16(Console.ReadLine());
                    if (armour_stats[1, to_buy - 1] <= Player.gold)
                    {
                        Player.armour = (armour[to_buy - 1]);
                        Player.defence = armour_stats[0, to_buy - 1] / 2;
                        Player.gold -= armour_stats[1, to_buy - 1];
                        Player.adefence = Player.defence + Player.defence_increase;
                        Console.WriteLine("You now have " + Player.armour);
                        Console.WriteLine("Your defence is now " + Player.adefence);
                        Console.WriteLine("Your gold is now " + Player.gold);
                    }
                    else
                    {
                        Console.WriteLine("You cannot afford this");
                    }
                    break;
                case "weapons":
                    for (int i = 0; i <= weapons.Length-1; i++)
                    {
                        Console.WriteLine(i + 1 + ":" + weapons[i] + " Damage: " + weapon_stats[0,i] + " Price: " + weapon_stats[1,i] + " Gold\n");
                    }
                    Console.WriteLine("\nWhat armour set would you like to buy?\n");
                    int wto_buy = Convert.ToInt16(Console.ReadLine());
                    if (weapon_stats[1, wto_buy - 1] <= Player.gold)
                    {
                        Player.weapon = (weapons[wto_buy - 1]);
                        Player.damage = weapon_stats[0, wto_buy - 1];
                        Player.gold -= weapon_stats[1, wto_buy - 1];
                        Player.adamage = Player.damage + Player.damage_increase;
                        Console.WriteLine("You now have " + Player.weapon);
                        Console.WriteLine("Your defence is now " + Player.adamage);
                        Console.WriteLine("Your gold is now " + Player.gold);
                    }
                    else
                    {
                        Console.WriteLine("You cannot afford this");
                    }
                    break;
                case "potions":
                    Console.WriteLine("Health potions are useful as they heal you, they cost " + Player.health_pots_price);
                    Console.WriteLine("How many health potions would you like to buy");
                    int amount = Convert.ToInt16(Console.ReadLine());
                    int price = Player.health_pots_price * amount;
                    if (price <= Player.gold)
                    {
                        Console.WriteLine("The cost for the health potions is " + price + " are you sure you wanna buy them after this you will have " + (Player.gold - price) + " gold\n");
                        String confirm = Convert.ToString(Console.ReadLine())!;
                        if (confirm.ToLower() == "yes")
                        {
                            Player.gold -= price;
                            Player.health_pots += amount;
                            Console.WriteLine("You have " + Player.health_pots + " health potions");
                            Console.WriteLine("Your gold is " + Player.gold);
                        }
                        else { Console.WriteLine("\n"); }
                    }
                    else { Console.WriteLine("You cannot afford this"); }
                    break;
                default:
                    Player.shop(Player);
                    break;
            }
        }
        public static void inv(Player Player)
        {
            Console.WriteLine("You have " + Player.gold + " gold");
            Console.WriteLine("The weapon you have equipped is " + Player.weapon + " which allows you to hit for " + Player.adamage);
            Console.WriteLine("You have " + Player.armour + " equipped with a defence of " + Player.adefence);
            Console.WriteLine("You have " + Player.health + " health");
            Console.WriteLine("You have " + Player.health_pots + " health potions");
            Console.WriteLine("YOu are level " + Player.level);
        }
        public static void heal(Player Player)
        {
            Random random = new Random();
            int health_pot_value = random.Next(10, 30);
            while (Player.health_pots > 0)
            {
                Console.WriteLine("Would you like to heal with a health potion\n");
                String action = Convert.ToString(Console.ReadLine())!;
                if (action.ToLower() == "yes")
                {
                    Player.health += health_pot_value;
                    Player.health_pots--;
                    if (Player.health > Player.max_health)
                    {
                        Player.health = Player.max_health;
                    }
                    Console.WriteLine("you have been healed your health is now "+Player.health);
                }
                else if (action.ToLower() == "no")
                {
                    playing(Player);
                }
                else
                {
                    Console.WriteLine("Please enter yes or no");
                    Player.heal(Player);
                }
            }
            if (Player.health_pots <= 0)
            {
                Console.WriteLine("It seems that you don't have any health potions,why don't you buy one");
            }
        }
        public static void levelling(Player Player)
        {
            Player.xp_needed = Player.xp + (int)Math.Round(((decimal)Player.level * 50) + 100);
            Player.level++;
            Player.max_health += Player.max_health / 50;
            Player.health = Player.max_health;
            Player.damage_increase += Player.adamage / 15;
            Player.defence_increase += Player.adefence / 15;
            Player.adamage = Player.damage + Player.damage_increase;
            Player.adefence = Player.defence + Player.defence_increase;
            Console.WriteLine("Do you want to boost your Defence,Damage or Health\n");
            String levelup_choice = Convert.ToString(Console.ReadLine())!;
            switch (levelup_choice.ToLower())
            {
                case "defence":
                    Player.adefence += Player.adefence / 25;
                    Console.WriteLine("You have chosen to strengthen your battlements against the hordes of enemies to a defence of" + Player.adefence);
                    break;
                case "damage":
                    Player.adamage += Player.adamage / 25;
                    Console.WriteLine("You have chosen to stiffen your blows against the hordes of enemies to hit for" + Player.adamage + " damage");
                    break;
                case "health":
                    Player.max_health += Player.max_health / 25;
                    Player.health = Player.max_health;
                    Console.WriteLine("You have chosen to increase your resolve against the hordes of enemies to a maximum of " + Player.max_health + " HP");
                    break;
                default:
                    Console.Write("YOu have chose to forfeit your chance to increase one stat furhter");
                    break;
            }
            Console.WriteLine("You have defeated enough monsters to level up to Level:"+ Player.level);
        }
        public static void playing(Player Player)
        {
            while (Player.alive == true) { 
                if (Player.xp > Player.xp_needed)
                {
                    Player.levelling(Player);
                }
                Console.WriteLine("What command do you want to input");
                String action = Convert.ToString(Console.ReadLine())!;
                switch (action.ToLower())
                {
                    case "inv":
                        Player.inv(Player);
                        playing(Player);
                        break;
                    case "commands":
                        Player.commands();
                        playing(Player);
                        break;
                    case "fight":
                        Player.Fight(Player);
                        playing(Player);
                        break;
                    case "shop":
                        Player.shop(Player);
                        playing(Player);
                        break;
                    case "heal":
                        Player.heal(Player);
                        playing(Player);
                        break;
                    default:
                        playing(Player);
                        break;
                }
            }
        }
        public static void idle(Player Player)
        {
            Console.WriteLine("Do you want to Play, leave or see commands");
            String choice = Convert.ToString(Console.ReadLine())!;
            if (choice.ToLower() == "play")
            {
                Console.WriteLine("You awake in a place you don't recognise and have a feeling you aren't safe there.");
                Player.alive = true;
                playing(Player);
            }
            else if (choice.ToLower() == "commands")
            {
                Player.commands();
                idle(Player);
            }
            else if (choice.ToLower() == "leave")
            {
                Environment.Exit(0);
            }
            else { idle(Player); }
        }
    }
    class Knight : Player
    {

        public Knight()
        {
            max_health = 150;
            health = 75;
            health_pots = 1;
            damage = 15;
            gold = 0;
            armour = "Armour of the Knightly warriors";
            weapon = "Sword of the Fallen Knight";
            level = 5;
            adamage = damage + damage_increase;
        }
        public override void Fight(Player Player)
        {
            Random random = new Random();
            String[] enemy = ["skeleton", "zombie", "slime", "ghost", "goblin", "rat"];
            int[,] enemy_stats = { { random.Next(15, 45), random.Next(5, 15), random.Next(5, 10), random.Next(1, 5), random.Next(20, 40), random.Next(1, 3) },
            { 15, 10, 5, 1, 13, 2 },
            { random.Next(45, 135), random.Next(15, 45), random.Next(10, 30), random.Next(5, 15), random.Next(40, 120), random.Next(3, 9)},
            { random.Next(15, 25), random.Next(3, 7), random.Next(3, 5), random.Next(1, 5), random.Next(12, 22), random.Next(1, 3)}};
            int index = random.Next(0, 5);
            String current_enemy = enemy[index];
            int ehealth;
            int edamage;
            if (Player.level < 2)
            {
                ehealth = enemy_stats[0, index];
                edamage = enemy_stats[1, index];
            }
            else
            {
                ehealth = (int)Math.Round(enemy_stats[0, index] * Math.Sqrt(Player.level));
                edamage = (int)Math.Round(enemy_stats[1, index] * Math.Sqrt(Player.level));
            }
            int reward = enemy_stats[2, index];
            int xp_reward = enemy_stats[3, index];
            Console.WriteLine("A " + current_enemy + " has appeared");
            Console.WriteLine("The " + current_enemy + " has " + ehealth + " health and does " + edamage + " damage");
            while (ehealth > 0 || Player.health > 0)
            {
                int edamage_done = (int)(edamage - Math.Round(((double)Player.defence / 5)));
                int luck = random.Next(0, 100) / 100;
                int effect = 1;
                if (luck >= 0.85)
                {
                    effect = 2;
                    Console.WriteLine("Your training as a knight allow you to hit for twice the damage");
                }
                if (edamage_done <= 0)
                {
                    Player.health -= 0;
                }
                else if (edamage_done > 0)
                {
                    Thread.Sleep(1500);
                    Console.WriteLine("You have " + Player.health + " health and the enemy has " + ehealth + " health");
                    Player.health -= edamage_done;
                    int damage_done = random.Next((Player.adamage - 5), (Player.adamage + 5));
                    if (damage_done <= 0)
                    {
                        ehealth -= 0;
                    }
                    else
                    {
                        ehealth -= damage_done * effect;
                    }
                }
                if (Player.health <= 0)
                {
                    if (Player.health_pots > 1)
                    {
                        Player.heal(Player);
                        Console.WriteLine("You make one last stand against the " + current_enemy);
                    }
                    else
                    {
                        Console.WriteLine("You have died");
                        Player.alive = false;
                        break;
                    }
                }
                if (ehealth <= 0)
                {
                    Player.gold += reward;
                    Player.xp += xp_reward;
                    Thread.Sleep(1500);
                    Console.WriteLine("The " + current_enemy + " has been slain");
                    Console.WriteLine("You have gained " + reward + " gold.You now have " + Player.gold + " gold");
                    Console.WriteLine("you gained " + xp_reward + " xp.You now have " + Player.xp + " xp");
                    Console.WriteLine("your health is " + Player.health);
                    playing(Player);
                }
            }
        }
    }
    class Merchant : Player
    {
        public Merchant()
        {
            Random random = new Random();
            max_health = 75;
            damage = 0;
            health_pots = 0;
            gold = random.Next(50, 150);
            armour = "Garbs of the Merchant Guilds";
            level = 3;
            health_pots_price = random.Next(5, 15);
            adamage = damage + damage_increase;
        }
        public override void Fight(Player Player)
        {
            Console.WriteLine("You have the choice to pay the monsters 15 gold to leave you alone");
            String choice = Convert.ToString(Console.ReadLine())!;
            if (choice.ToLower() == "yes")
            {
                if (Player.gold >= 15)
                {
                    Player.gold -= 15;
                    Console.WriteLine("They take your gold and leave you be... for now");
                    return ;
                }
                else
                {
                    Console.WriteLine("Your measly offering was not sufficient");
                }
            }
            else
            {
                Console.WriteLine("Have it your way");
            }
            Random random = new Random();
            String[] enemy = ["skeleton", "zombie", "slime", "ghost", "goblin", "rat"];
            int[,] enemy_stats = { { random.Next(15, 45), random.Next(5, 15), random.Next(5, 10), random.Next(1, 5), random.Next(20, 40), random.Next(1, 3) },
            { 15, 10, 5, 1, 13, 2 },
            { random.Next(45, 135), random.Next(15, 45), random.Next(10, 30), random.Next(5, 15), random.Next(40, 120), random.Next(3, 9)},
            { random.Next(15, 25), random.Next(3, 7), random.Next(3, 5), random.Next(1, 5), random.Next(12, 22), random.Next(1, 3)}};
            int index = random.Next(0, 5);
            String current_enemy = enemy[index];
            int ehealth;
            int edamage;
            if (Player.level < 2)
            {
                ehealth = enemy_stats[0, index];
                edamage = enemy_stats[1, index];
            }
            else
            {
                ehealth = (int)Math.Round(enemy_stats[0, index] * Math.Sqrt(Player.level));
                edamage = (int)Math.Round(enemy_stats[1, index] * Math.Sqrt(Player.level));
            }
            int reward = enemy_stats[2, index];
            int xp_reward = enemy_stats[3, index];
            Console.WriteLine("A " + current_enemy + " has appeared");
            Console.WriteLine("The " + current_enemy + " has " + ehealth + " health and does " + edamage + " damage");
            while (ehealth > 0 || Player.health > 0)
            {
                int edamage_done = (int)(edamage - Math.Round(((double)Player.defence / 5)));
                if (edamage_done <= 0)
                {
                    Player.health -= 0;
                }
                else if (edamage_done > 0)
                {
                    Thread.Sleep(1500);
                    Console.WriteLine("You have " + Player.health + " health and the enemy has " + ehealth + " health");
                    Player.health -= edamage_done;
                    int damage_done = random.Next((Player.adamage - 5), (Player.adamage + 5));
                    if (damage_done <= 0)
                    {
                        ehealth -= 0;
                    }
                    else
                    {
                        ehealth -= damage_done;
                    }
                }
                if (Player.health <= 0)
                {
                    if (Player.health_pots > 1)
                    {
                        Player.heal(Player);
                        Console.WriteLine("You make one last stand against the " + current_enemy);
                    }
                    else
                    {
                        Console.WriteLine("You have died");
                        Player.alive = false;
                        break;
                    }
                }
                if (ehealth <= 0)
                {
                    Player.gold += reward;
                    Player.xp += xp_reward;
                    Thread.Sleep(1500);
                    Console.WriteLine("The " + current_enemy + " has been slain");
                    Console.WriteLine("You have gained " + reward + " gold.You now have " + Player.gold + " gold");
                    Console.WriteLine("you gained " + xp_reward + " xp.You now have " + Player.xp + " xp");
                    Console.WriteLine("your health is " + Player.health);
                    playing(Player);
                }
            }
        }
    }    
    class Healer : Player
    {
            public Healer()
            {
                Random random = new Random();
                health_pots = 12;
                damage = 1;
                defence = 15;
                gold = 10;
                armour = "Finery of the healer clergy";
                level = 2;
                health_pots_price = random.Next(5, 15);
                adamage = damage + damage_increase;
            }
            public override void Fight(Player Player)
            {
                Random random = new Random();
                String[] enemy = ["skeleton", "zombie", "slime", "ghost", "goblin", "rat"];
                int[,] enemy_stats = { { random.Next(15, 45), random.Next(5, 15), random.Next(5, 10), random.Next(1, 5), random.Next(20, 40), random.Next(1, 3) },
            { 15, 10, 5, 1, 13, 2 },
            { random.Next(45, 135), random.Next(15, 45), random.Next(10, 30), random.Next(5, 15), random.Next(40, 120), random.Next(3, 9)},
            { random.Next(15, 25), random.Next(3, 7), random.Next(3, 5), random.Next(1, 5), random.Next(12, 22), random.Next(1, 3)}};
                int index = random.Next(0, 5);
                String current_enemy = enemy[index];
                int ehealth;
                int edamage;
                if (Player.level < 2)
                {
                    ehealth = enemy_stats[0, index];
                    edamage = enemy_stats[1, index];
                }
                else
                {
                    ehealth = (int)Math.Round(enemy_stats[0, index] * Math.Sqrt(Player.level));
                    edamage = (int)Math.Round(enemy_stats[1, index] * Math.Sqrt(Player.level));
                }
                int reward = enemy_stats[2, index];
                int xp_reward = enemy_stats[3, index];
                Console.WriteLine("A " + current_enemy + " has appeared");
                Console.WriteLine("The " + current_enemy + " has " + ehealth + " health and does " + edamage + " damage");
                while (ehealth > 0 || Player.health > 0)
                {
                    int edamage_done = (int)(edamage - Math.Round(((double)Player.defence / 5)));
                    int luck = random.Next(0, 100) / 100;
                    int effect = 1;
                    if (luck >= 0.85)
                    {
                        effect = 0;
                        Console.WriteLine("Your heightened senses of danger have allowed you to avoid the enemies attack");
                    }
                    if (edamage_done <= 0)
                    {
                        Player.health -= 0;
                    }
                    else if (edamage_done > 0)
                    {
                        Thread.Sleep(1500);
                        Console.WriteLine("You have " + Player.health + " health and the enemy has " + ehealth + " health");
                        Player.health -= edamage_done;
                        int damage_done = random.Next((Player.adamage - 5), (Player.adamage + 5));
                        if (damage_done <= 0)
                        {
                            ehealth -= 0;
                        }
                        else
                        {
                            ehealth -= damage_done * effect;
                        }
                    }
                    if (Player.health <= 0)
                    {
                        if (Player.health_pots > 1)
                        {
                            Player.heal(Player);
                            Console.WriteLine("You make one last stand against the " + current_enemy);
                        }
                        else
                        {
                            Console.WriteLine("You have died");
                            Player.alive = false;
                            break;
                        }
                    }
                    if (ehealth <= 0)
                    {
                        Player.gold += reward;
                        Player.xp +=  xp_reward;
                        Thread.Sleep(1500);
                        Console.WriteLine("The " + current_enemy + " has been slain");
                        Console.WriteLine("You have gained " + reward + " gold.You now have " + Player.gold + " gold");
                        Console.WriteLine("you gained " + xp_reward + " xp.You now have " + Player.xp + " xp");
                        Console.WriteLine("your health is " + Player.health);
                        playing(Player);
                    }
                }
            }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Do you want to be play as the knight, merchant, healer, or base class");
            String choice = Convert.ToString(Console.ReadLine())!;
            
            switch (choice.ToLower())
            {
                case "knight":
                    Console.WriteLine("You have chosen to become a fallen Knight: Wounded yet Noble");
                    Knight knight = new Knight();
                    Knight.idle(knight);
                    break;
                case "merchant":
                    Console.WriteLine("You have chosen to be become a wealthy merchant of the guilds: Rich and Vain");
                    Merchant merchant = new Merchant();
                    Merchant.idle(merchant);
                    break;
                case "healer":
                    Console.WriteLine("You have chosen to become a healer of the clerical class: Regal yet Tough");
                    Healer healer = new Healer();
                    Healer.idle(healer);
                    break;
                default:
                    Console.WriteLine("Base class then");
                    Player character = new Player();
                    Player.idle(character);
                    break;
            }
        }
    }
}
