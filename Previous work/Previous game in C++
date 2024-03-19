#include <iostream>
#include <string>
#include <random>
#include <cmath>
#include <chrono>
#include <thread>

class Player{
    public:
         int max_health;
         int health;
         int health_pots;
         int damage;
         int defence;
         int gold;
         std::string armour;
         std::string weapon;
         bool alive;
         int level;
         int xp;
         int xp_needed;
         int health_pots_price;
         int damage_increase;
         int defence_increase;
         int adamage;
         int adefence;

    Player(){
            max_health = 100;
            health = max_health;
            health_pots = rand()%6;
            damage = 5;
            defence = 0;
            gold = rand()%30+10;
            armour = "No Armour";
            weapon = "No Weapon";
            alive = false;
            level = 1;
            xp = 0;
            xp_needed = xp + (level * 50) + 100;
            health_pots_price = rand()%30+10;
            damage_increase = 0;
            defence_increase = 0;
            adamage = damage + damage_increase;
            adefence = defence + defence_increase;
    }

    void commands(){
        std::cout << "use the inv command for your inventory\n";
        std::cout << "use the fight command to fight an enemy\n";
        std::cout << "use the shop command to buy equipment from a shop\n";
        std::cout << "use the heal command to use health potions\n";
    }

    void fight(Player Player){
        std::string enemy[6] = {"skeleton", "zombie", "slime", "ghost", "goblin", "rat"};
        int enemy_stats[4] [6]= { { rand()%31+15, rand()%11+5, rand()%6+5, rand()%5+1, rand()%21+20, rand()%3+1 },
            { 15, 10, 5, 1, 13, 2 },
            { rand()%91+45, rand()%31+15, rand()%21+10, rand()%11+5, rand()%81+40, rand()%7+3},
            { rand()%11+15, rand()%5+3, rand()%3+3,rand()%5+1,rand()%11+12, rand()%3+1}};
        int index = rand()%6;
        std::string current_enemy = enemy[index];
        int ehealth;
        int edamage;
        if (Player.level<2){
            ehealth = enemy_stats[0][index];
            edamage = enemy_stats[1][index];
        }else{
            ehealth = round(enemy_stats[0][index]*(sqrt(Player.level)));
            edamage = round(enemy_stats[1][index]*(sqrt(Player.level)));
            }
        int reward = enemy_stats[2][index];
        int xp_reward = enemy_stats[3][index];
        std::cout << "A " << current_enemy << " has appeared\n";
        std::cout << "The " << current_enemy << " has " << ehealth << " health and does " << edamage << " damage\n";
        while(ehealth > 0 || Player.health>0){
            int edamage_done = edamage - round(Player.defence/5);
            if(edamage_done<=0){
                Player.health-=0;
            }else{
                std::this_thread::sleep_for(std::chrono::milliseconds(1500));
                std::cout << "You have "<<Player.health << " health and the enemy has " << ehealth << "health\n";
                Player.health-=edamage_done;
                int damage_done = rand()%(Player.defence+5);
                if(damage_done<=0){
                    ehealth-=0;
                }else{
                    ehealth-=damage_done;
                }
            }
            if(Player.health<=0){
                if(Player.health_pots>=1){
                    Player.heal(Player);
                    std::cout << "You make one last stand against the " <<current_enemy << "\n";
                }else{
                    std::cout << "You have died\n";
                    Player.alive=false;
                    break;
                }
            }
            if(ehealth<=0){
                Player.gold+=reward;
                Player.xp+=xp_reward;
                std::this_thread::sleep_for(std::chrono::milliseconds(1500));
                std::cout << "The " << current_enemy << "has been slain\n";
                std::cout << "You have gained" << reward << " gold. You now have " << Player.gold << " gold\n";
                std::cout << "You gained " << xp_reward << " xp. You now have " << Player.xp << " xp\n";
                std::cout << "Your health is " <<Player.health << "\n";    
                Player.playing(Player);            
            }
        }
    }
    
    void shop(Player Player){
        std::string armour[5] = {"leather armour", "bronze armour", "steel armour", "obsidian armour", "ancient armour"};
        int armour_stats[2][5]={ { 5, 10, 20, 25, 50 }, { 25, 30, 50, 60, 120 } };
        std::string weapons[5]={"rusty sword", "steel sword", "knife", "rusty knife", "gold sword"};
        int weapon_stats[2][5]={ { 8, 15, 11, 7, 20 }, { 25, 50, 35, 15, 65 } };
        std::cout << "Would you like to see the armour, weapons, or potions\n";
        std::string choice;
        std::cin >> choice;
        int to_buy;
        if(choice=="armour"){
            for(int i=0;i<5;i++){
                std::cout << i+1 << ": " << armour[i] << " Defence: " << armour_stats[0][i] << " Price: " << armour_stats[1][i] << " Gold\n";
            }
            std::cout << "\nWhat armour set would you like to buy?\n";
            std::cin >> to_buy;
            if(armour_stats[1][to_buy-1] <= Player.gold){
                        Player.armour = (armour[to_buy - 1]);
                        Player.defence = armour_stats[0][to_buy - 1] / 2;
                        Player.gold -= armour_stats[1][to_buy - 1];
                        Player.adefence = Player.defence + Player.defence_increase;
                        std::cout << "You now have " << Player.armour << "\n";
                        std::cout << "Your defence is now " << Player.adefence << "\n";
                        std::cout << "Your gold is now " << Player.gold << "\n";
            }else{
                std::cout << "You cannot afford this\n";
            }
        }else if(choice=="weapons"){
            for(int i = 0;i<5;i++){
                std::cout << i+1 << ": " << weapons[i] << " Damage: " << weapon_stats[0][i] << " Price: " << weapon_stats[1][i] << " Gold\n";
            }
            std::cout << "What weapon would you like to buy\n";
            std::cin >> to_buy;
            if(weapon_stats[1][to_buy-1] <= Player.gold){
                        Player.weapon = weapons[to_buy - 1];
                        Player.damage = weapon_stats[0] [to_buy - 1];
                        Player.gold -= weapon_stats[1][to_buy - 1];
                        Player.adamage = Player.damage + Player.damage_increase;
                        std::cout <<"You now have " << Player.weapon << "\n";
                        std::cout <<"Your defence is now " << Player.adamage << "\n";
                        std::cout <<"Your gold is now " << Player.gold << "\n";
            }else{
                std::cout << "You cannot afford this\n";
            }
        }else if(choice=="potions"){
            std::cout << "Health potions are useful as they heal you, they cost " << Player.health_pots_price << "\n";
            std::cout << "How many health potions would you like to buy\n";
            int amount;
            std::cin >> amount;
            int price = Player.health_pots_price*amount;
            if(price <= Player.gold){
                std::cout << "The cost for the health potions is " << price << " are you sure you wannna buy them, after this you will have " << (Player.gold-price) << " gold\n";
                std::string confirm;
                std::cin >> confirm;
                if(confirm=="yes"){
                    Player.gold-=price;
                    Player.health_pots +=amount;
                    std::cout << "You have " << Player.health_pots << "health potions\n";
                    std::cout << "Your gold is " << Player.gold << "\n";
                }else{
                    std::cout << "\n";
                }
            }else{
                std::cout << "You cannot afford this\n";
            }
        }else{
            Player.shop(Player);
        }
    }
    void inv(Player Player){
            std::cout << "You have " << Player.gold << " gold\n";
            std::cout << "The weapon you have equipped is " << Player.weapon << " which allows you to hit for " << Player.adamage << "\n";
            std::cout << "You have " << Player.armour << " equipped with a defence of " << Player.adefence << "\n";
            std::cout << "You have " << Player.health << " health\n";
            std::cout << "You have " << Player.health_pots << " health potions\n";
            std::cout << "You are level " << Player.level << "\n";
    }
    void heal(Player Player){
        int health_pot_value=rand()%20+10;
        while(Player.health_pots>0){
            std::cout << "Would you like to heal with a health potion\n";
            std::string action;
            std::cin >> action;
            if(action == "yes"){
                Player.health+=health_pot_value;
                Player.health_pots--;
                if(Player.health>Player.max_health){
                    Player.health=Player.max_health;
                }
                std::cout << "You have been healed, your health is now " << Player.health << "\n";
            }else if(action=="no"){
                Player.playing(Player);
            }else{
                std::cout << "Please enter yes or no\n";
                Player.heal(Player);
            }
        }
        if(Player.health_pots<=0){
            std::cout << "It seems that you don't have any health potions,why don't you buy one \n";
        }
    }
    void levelling(Player Player){
            Player.xp_needed = Player.xp + Player.level * 50 + 100;
            Player.level++;
            Player.max_health += Player.max_health / 50;
            Player.health = Player.max_health;
            Player.damage_increase += Player.adamage / 15;
            Player.defence_increase += Player.adefence / 15;
            Player.adamage = Player.damage + Player.damage_increase;
            Player.adefence = Player.defence + Player.defence_increase;
            std::cout << "Do you want to boost your Defence, Damage, or Health\n";
            std::string choice;
            std::cin >> choice;
            if(choice == "defence"){
                Player.adefence+=Player.adefence/25;
                std::cout << "You have chosen to strengthen your battlements against the hordes of enemies to a defence of " << Player.adefence << "\n";
            }else if(choice == "damage"){
                Player.adamage += Player.adamage / 25;
                std::cout << "You have chosen to stiffen your blows against the hordes of enemies to hit for " << Player.adamage + " damage\n";
            }else if(choice=="health"){
                Player.max_health += Player.max_health / 25;
                Player.health = Player.max_health;
                std::cout << "You have chosen to increase your resolve against the hordes of enemies to a maximum of " << Player.max_health + " HP\n";
            }else{
                std::cout << "You have chosen to forfeit your chance to increase one stat further\n";
            }
            std::cout << "You have defeated enough monsters to level up to Level:" << Player.level << "\n";
    }
    void playing(Player Player){
        while(Player.alive==true){
            if(Player.xp>=Player.xp_needed){
                Player.levelling(Player);
            }
            std::cout << "What command do you want to input\n";
            std::string action;
            std::cin >> action;
            if(action == "inv"){
                Player.inv(Player);
                Player.playing(Player);
            }else if(action == "commands"){
                Player.commands();
                Player.playing(Player);
            }else if(action == "fight"){
                Player.fight(Player);
                Player.playing(Player);
            }else if(action == "shop"){
                Player.shop(Player);
                Player.playing(Player);
            }else if(action == "heal"){
                Player.heal(Player);
                Player.playing(Player);
            }else{
                Player.playing(Player);
            }
        }
    }
    void idle(Player Player){
        std::cout << "Do you want to Play, leave, or see commands\n";
        std::string choice;
        std::cin >> choice;
        if(choice=="play"){
            std::cout << "You awake in a place you don't recognise and have a feeling you aren't safe there.\n";
            Player.alive=true;
            Player.playing(Player);
        }else if(choice == "commands"){
            Player.commands();
            Player.idle(Player);
        }else if(choice=="leave"){
            exit(0);
        }else{
            Player.idle(Player);
        }
    }
};

class Knight : public Player{
    public:
    Knight(){
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
    void fight(Player Player){
        std::string enemy[6] = {"skeleton", "zombie", "slime", "ghost", "goblin", "rat"};
        int enemy_stats[4] [6]= { { rand()%31+15, rand()%11+5, rand()%6+5, rand()%5+1, rand()%21+20, rand()%3+1 },
            { 15, 10, 5, 1, 13, 2 },
            { rand()%91+45, rand()%31+15, rand()%21+10, rand()%11+5, rand()%81+40, rand()%7+3},
            { rand()%11+15, rand()%5+3, rand()%3+3,rand()%5+1,rand()%11+12, rand()%3+1}};
        int index = rand()%6;
        std::string current_enemy = enemy[index];
        int ehealth;
        int edamage;
        if (Player.level<2){
            ehealth = enemy_stats[0][index];
            edamage = enemy_stats[1][index];
        }else{
            ehealth = round(enemy_stats[0][index]*(sqrt(Player.level)));
            edamage = round(enemy_stats[1][index]*(sqrt(Player.level)));
            }
        int reward = enemy_stats[2][index];
        int xp_reward = enemy_stats[3][index];
        std::cout << "A " << current_enemy << " has appeared\n";
        std::cout << "The " << current_enemy << " has " << ehealth << " health and does " << edamage << " damage\n";
        while(ehealth > 0 || Player.health>0){
            int edamage_done = edamage - round(Player.defence/5);
            int luck = rand()%101/100;
            int effect=1;
            if(luck>=0.85){
                effect=2;
                std::cout << "Your training as a knight allow you to hit for twice the damage\n";
            }
            if(edamage_done<=0){
                Player.health-=0;
            }else{
                std::this_thread::sleep_for(std::chrono::milliseconds(1500));
                std::cout << "You have "<<Player.health << " health and the enemy has " << ehealth << " health\n";
                Player.health-=edamage_done;
                int damage_done = rand()%(Player.defence+5);
                if(damage_done<=0){
                    ehealth-=0;
                }else{
                    ehealth-=damage_done*effect;
                }
            }
            if(Player.health<=0){
                if(Player.health_pots>=1){
                    Player.heal(Player);
                    std::cout << "You make one last stand against the " << current_enemy << "\n";
                }else{
                    std::cout << "You have died\n";
                    Player.alive=false;
                    break;
                }
            }
            if(ehealth<=0){
                Player.gold+=reward;
                Player.xp+=xp_reward;
                std::this_thread::sleep_for(std::chrono::milliseconds(1500));
                std::cout << "The " << current_enemy << " has been slain\n";
                std::cout << "You have gained" << reward << " gold. You now have " << Player.gold << " gold\n";
                std::cout << "You gained " << xp_reward << " xp. You now have " << Player.xp << " xp\n";
                std::cout << "Your health is " <<Player.health << "\n";    
                Player.playing(Player);            
            }
        }
    }
};

class merchant:public Player{
    public:
    merchant(){
            max_health = 75;
            damage = 0;
            health_pots = 0;
            gold = rand()%101+50;
            armour = "Garbs of the Merchant Guilds";
            level = 3;
            health_pots_price = rand()%11+5;
            adamage = damage + damage_increase;
    }
        void fight(Player Player){
            std::cout << "You have the choice to pay the monsters 15 gold to leave you alone\n";
            std::string choice;
            std::cin >> choice;
            if(choice=="yes"){
                if(Player.gold>=15){
                    Player.gold-=15;
                    std::cout << "They take your gold and leave you be... for now\n";
                    return ;
                }else{
                    std::cout << "Your measly offering was not sufficient\n";
                }
            }else{
                std::cout << "Have it your way\n";
            }
            std::string enemy[6] = {"skeleton", "zombie", "slime", "ghost", "goblin", "rat"};
            int enemy_stats[4] [6]= { { rand()%31+15, rand()%11+5, rand()%6+5, rand()%5+1, rand()%21+20, rand()%3+1 },
            { 15, 10, 5, 1, 13, 2 },
            { rand()%91+45, rand()%31+15, rand()%21+10, rand()%11+5, rand()%81+40, rand()%7+3},
            { rand()%11+15, rand()%5+3, rand()%3+3,rand()%5+1,rand()%11+12, rand()%3+1}};
            int index = rand()%6;
            std::string current_enemy = enemy[index];
            int ehealth;
            int edamage;
            if (Player.level<2){
                ehealth = enemy_stats[0][index];
                edamage = enemy_stats[1][index];
            }else{
                ehealth = round(enemy_stats[0][index]*(sqrt(Player.level)));
                edamage = round(enemy_stats[1][index]*(sqrt(Player.level)));
                }
            int reward = enemy_stats[2][index];
            int xp_reward = enemy_stats[3][index];
            std::cout << "A " << current_enemy << " has appeared\n";
            std::cout << "The " << current_enemy << " has " << ehealth << " health and does " << edamage << " damage\n";
            while(ehealth > 0 || Player.health>0){
                int edamage_done = edamage - round(Player.defence/5);
                if(edamage_done<=0){
                    Player.health-=0;
                }else{
                    std::this_thread::sleep_for(std::chrono::milliseconds(1500));
                    std::cout << "You have "<<Player.health << " health and the enemy has " << ehealth << " health\n";
                    Player.health-=edamage_done;
                    int damage_done = rand()%(Player.defence+5);
                    if(damage_done<=0){
                        ehealth-=0;
                    }else{
                        ehealth-=damage_done;
                    }
                }
                if(Player.health<=0){
                    if(Player.health_pots>=1){
                        Player.heal(Player);
                        std::cout << "You make one last stand against the " <<current_enemy << "\n";
                    }else{
                        std::cout << "You have died\n";
                        Player.alive=false;
                        break;
                    }
                }
                if(ehealth<=0){
                    Player.gold+=reward;
                    Player.xp+=xp_reward;
                    std::this_thread::sleep_for(std::chrono::milliseconds(1500));
                    std::cout << "The " << current_enemy << " has been slain\n";
                    std::cout << "You have gained" << reward << " gold. You now have " << Player.gold << " gold\n";
                    std::cout << "You gained " << xp_reward << " xp. You now have " << Player.xp << " xp\n";
                    std::cout << "Your health is " <<Player.health << "\n";    
                    Player.playing(Player);            
                }
        }    
    }
};

class healer : public Player{
    public:
    healer(){
        health_pots = 12;
        damage = 1;
        defence = 15;
        gold = 10;
        armour = "Finery of the healer clergy";
        level = 2;
        health_pots_price = rand()%11+5;
        adamage = damage + damage_increase;
    }
    void fight(Player Player){
        std::string enemy[6] = {"skeleton", "zombie", "slime", "ghost", "goblin", "rat"};
        int enemy_stats[4] [6]= { { rand()%31+15, rand()%11+5, rand()%6+5, rand()%5+1, rand()%21+20, rand()%3+1 },
            { 15, 10, 5, 1, 13, 2 },
            { rand()%91+45, rand()%31+15, rand()%21+10, rand()%11+5, rand()%81+40, rand()%7+3},
            { rand()%11+15, rand()%5+3, rand()%3+3,rand()%5+1,rand()%11+12, rand()%3+1}};
        int index = rand()%6;
        std::string current_enemy = enemy[index];
        int ehealth;
        int edamage;
        if (Player.level<2){
            ehealth = enemy_stats[0][index];
            edamage = enemy_stats[1][index];
        }else{
            ehealth = round(enemy_stats[0][index]*(sqrt(Player.level)));
            edamage = round(enemy_stats[1][index]*(sqrt(Player.level)));
            }
        int reward = enemy_stats[2][index];
        int xp_reward = enemy_stats[3][index];
        std::cout << "A " << current_enemy << " has appeared\n";
        std::cout << "The " << current_enemy << " has " << ehealth << " health and does " << edamage << " damage\n";
        while(ehealth > 0 || Player.health>0){
            int edamage_done = edamage - round(Player.defence/5);
            int luck = rand()%101/100;
            int effect=1;
            if(luck>=0.85){
                effect=0;
                std::cout << "Your heightened senses of danger have allowed you to avoid the enemies attack\n";
            }
            if(edamage_done<=0){
                Player.health-=0;
            }else{
                std::this_thread::sleep_for(std::chrono::milliseconds(1500));
                std::cout << "You have "<<Player.health << " health and the enemy has " << ehealth << " health\n";
                Player.health-=edamage_done;
                int damage_done = rand()%(Player.defence+5);
                if(damage_done<=0){
                    ehealth-=0;
                }else{
                    ehealth-=damage_done*effect;
                }
            }
            if(Player.health<=0){
                if(Player.health_pots>=1){
                    Player.heal(Player);
                    std::cout << "You make one last stand against the " <<current_enemy << "\n";
                }else{
                    std::cout << "You have died\n";
                    Player.alive=false;
                    break;
                }
            }
            if(ehealth<=0){
                Player.gold+=reward;
                Player.xp+=xp_reward;
                std::this_thread::sleep_for(std::chrono::milliseconds(1500));
                std::cout << "The " << current_enemy << " has been slain\n";
                std::cout << "You have gained" << reward << " gold. You now have " << Player.gold << " gold\n";
                std::cout << "You gained " << xp_reward << " xp. You now have " << Player.xp << " xp\n";
                std::cout << "Your health is " << Player.health << "\n";       
                Player.playing(Player);            
            }
        }
    }
};

int main(){
    std::cout << "Do you want to be play as the knight, merchant, healer, or base class\n";
    std::string choice;
    std::cin >> choice;
    if(choice == "knight"){
        std::cout << "You have chosen to become a fallen Knight: Wounded yet Noble\n";
        Knight character;
        character.idle(character);       
    }else if(choice == "merchant"){
        std::cout << "You have chosen to be become a wealthy merchant of the guilds: Rich and Vain\n";
        merchant character;
        character.idle(character);
    }else if(choice == "healer"){
        std::cout << "You have chosen to become a healer of the clerical class: Regal yet Tough\n";
        healer character;
        character.idle(character);
    }else{
        Player character;
        character.idle(character);
    }
    return 0;
}
