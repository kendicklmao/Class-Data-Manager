#include<bits/stdc++.h>
#include<chrono>
#include<thread>
#include<fstream>
#include <filesystem>
#include <cstdlib>
using namespace std;
string get_save_path(){
    const char* appdata = getenv("LOCALAPPDATA");
    string path = string(appdata) + "\\GardenIdleTycoon";
    filesystem::create_directories(path);
    return path + "\\save.txt";
}

class Cash{ //Tài nguyên game
    private:
        double cash_amount;//Tổng tài nguyên
    public:
        Cash(){
            this->cash_amount = 0;//Tài nguyên ban đầu = 0
        }
        void add(double n){//Tăng thêm tài nguyên khi bán cây
            this->cash_amount += n;
        }
        bool withdraw(double n){//Sử dụng tài nguyên để mua bán
            if (this->cash_amount >= n){
                this->cash_amount -= n;
                return true;
            }
            return false;
        }
        double get(){
            return this->cash_amount;
        }
        void set(double n){
            this->cash_amount = n;
        }
};

class Gem{//Tài nguyên game cao cấp
    private:
        int gem_amount;//Tổng tài nguyên game cao cấp
    public:
        Gem(){
            this->gem_amount = 10;//Tài nguyên ban đầu = 10
        }
        void add(){//Tăng thêm tài nguyên khi nâng cấp đủ số lần
            this->gem_amount ++;
        }
        bool withdraw(){//Sử dụng tài nguyên để mua bán
            if (this->gem_amount >= 1){
                this->gem_amount --;
                return true;
            }
            return false;
        }
        int get(){//lấy số gem hiện có
            return this->gem_amount;
        }
        void set(int n){//lưu số tiền hiện có
            this->gem_amount = n;
        }
};

class Garden{//Vườn cây
    private:
        double cash_per_sec;//Giá tiền cây mỗi giây bán
        int level;//Cấp độ của vườn cây
        double upgrade_cost;//giá để nâng cấp vườn cây
        int add_gem = 10;//Mốc để cộng gem
    public:
        Garden(){//khởi tạo vườn ban đầu
            this->cash_per_sec = 1.0;
            this->level = 1;
            this->upgrade_cost = 10.0;
        }
        Garden(int n){//mua thêm vườn
            this->cash_per_sec = 1.0 + 0.5 * n;
            this->level = 1;
            this->upgrade_cost = 10.0 * (n + 1);
        }
        void work(Cash& cash, double time){//Nhận tiền bán cây
            cash.add(cash_per_sec * time);
        }
        bool upgrade(Cash& cash, Gem& gem, int n){//Nâng cấp vườn
            if (cash.withdraw(this->upgrade_cost) == true){
                this->level ++;
                this->cash_per_sec += (0.1 * (n + 1));
                this->upgrade_cost *= 1.5;
                if (level == add_gem){
                    this->add_gem += 10;
                    gem.add();
                }
                cout << "Upgrade succesful!" << "\n";
                return true;
            }
            else{
                cout << "Do you want to use gem for upgrading ?" << "\n";
                cout << "[1]. Yes" <<"\n";
                cout << "[2]. No" << "\n";
                char choice;
                cin >> choice;
                if (choice == '1'){
                    if (gem.withdraw() == true){
                        this->level ++;
                        this->cash_per_sec += 0.1;
                        this->upgrade_cost *= 1.5;
                        if (level == add_gem){
                            this->add_gem += 10;
                            gem.add();
                        }
                        cout << "Upgrade succesful!" << "\n";
                        return true;
                    }
                    else{
                        cout << "Not enough gem!" << "\n";
                        return false;
                    }
                }
                else{
                    cout << "Not enough cash!" << "\n";
                    return false;
                }
            }
        }
        void display_garden_attribute(){ //Hiển thị thông tin vườn cây
            cout << "Garden level: " << this->level << "\n";
            cout << "Cash/sec: " << this->cash_per_sec << "\n";
            cout << "Upgrade cost: " << this->upgrade_cost << "\n";
            cout << "extra gem: " << this->level % 10 << "/10" << "\n";
        }
        int get_level(){//lấy cấp độ
            return this->level;
        }
        double get_cash_per_sec(){//lấy số tiền trong 1 giây
            return this->cash_per_sec;
        }
        double get_upgrade_cost(){//lấy giá nâng cấp
            return this->upgrade_cost;
        }
        int get_add_gem(){//lấy số gem
            return this->add_gem;
        }
        void set_add_gem(int add_gem){//lưu số gem
            this->add_gem = add_gem;
        }
        void set_level(int level){//lưu cấp độ
            this->level = level;
        }
        void set_cash_per_sec(double cash_per_sec){
            this->cash_per_sec = cash_per_sec;
        }
        void set_upgrade_cost(double upgrade_cost){
            this->upgrade_cost = upgrade_cost;
        }
};

class Player{//Người chơi
    private:
        Cash cash;//Sở hữu tiền
        Gem gem;//Sở hữu gem
        vector<Garden> gardens;//Sở hữu vườn cây
        double garden_cost = 50.0;//giá mua thêm vườn
        int status = 1;//thứ sự vườn
    public:
        Player(){
            gardens.push_back(Garden());
        }
        void update(double time){//Cập nhật tiền theo thời gian
            for (Garden& g : this->gardens){
                g.work(this->cash, time);
            }
        }
        void upgrade_garden(int i){//nâng cấp vườn cây                                                                                                       
            if (i < 0 || i >= this->gardens.size()){
                cout << "Invalid garden!" << "\n";
                return;
            }
            else{
                gardens[i].upgrade(this->cash, this->gem, this->status);
            }
        }
        void buy_garden(){//mua thêm vườn
            if (cash.withdraw(this->garden_cost) == true){
                this->gardens.push_back(Garden(this->status));
                status ++;
                garden_cost *= 2;
                cout << "Buy succesfull!" << "\n";
            }
            else{
                cout << "Do you want to use gem for buying?" << "\n";
                cout << "[1] Yes" << "\n";
                cout << "[2] No" << "\n";
                char choice;
                cin >> choice;
                if (choice == '1'){
                    this->gardens.push_back(Garden(this->status));
                    status ++;
                    garden_cost *= 2;
                    gem.withdraw();
                    cout << "Buy succesfull!" << "\n";
                }
                else{
                    cout << "Buy failed!" << "\n";
                }
            }
        }
        void statis(){//Hiển thị trạng thái
            cout << "-----------------------" << "\n";
            cout << fixed << setprecision(2) << "Cash: " << cash.get() <<"\n";
            cout << "Gem: " << gem.get() << "\n";
            cout << "-----------------------" << "\n";
        }
        void display_garden(){//Hiện thị danh sách vườn
            int i = 1;
            for (Garden& g : this->gardens){
                cout << "Garden " << i << "\n";
                g.display_garden_attribute();
                i ++;
                cout << "\n";
            }
        }
        double get_garden_cost(){
            return this->garden_cost;
        }
        void set_garden_cost(double n){
            this->garden_cost = n;
        }
        int get_status(){
            return this->status;
        }
        void set_status(int n){
            this->status = n;
        }
        void save_game(){//lưu game
            ofstream file(get_save_path());
            if (!file.is_open()){
                return;
            }
            file << this->cash.get() << "\n";
            file << this->gem.get() << "\n";
            file << this->status << "\n";
            for (int i = 0; i < status; i ++){
                file << gardens[i].get_level() << "\n";
                file << gardens[i].get_cash_per_sec() << "\n";
                file << gardens[i].get_upgrade_cost() << "\n";
                file << gardens[i].get_add_gem() << "\n";
            }
            file << this->garden_cost;
            file.close();
        }
        void load_game(){//mở lại game
            ifstream file(get_save_path());
            if (!file.is_open()){
                return;
            }
            double cash_amount, cash_per_sec, upgrade_cost, garden_cost;
            int gem_amount, level, add_gem, status;
            vector<Garden> gardens;
            file >> cash_amount;
            file >> gem_amount;
            file >> status;
            for (int i = 0; i < status; i ++){
                file >> level;
                file >> cash_per_sec;
                file >> upgrade_cost;
                file >> add_gem;
                Garden g;
                g.set_level(level);
                g.set_cash_per_sec(cash_per_sec);
                g.set_upgrade_cost(upgrade_cost);
                g.set_add_gem(add_gem);
                gardens.push_back(g);
            }
            this->gardens.clear();
            for (Garden& g : gardens){
                this->gardens.push_back(g);
            }
            file >> garden_cost;
            this->cash.set(cash_amount);
            this->gem.set(gem_amount);
            this->garden_cost = garden_cost;
            this->status = status;
            file.close();
        }
};

int main(){
    Player player;
    player.load_game();
    auto last_time = chrono::steady_clock::now();
    while (true){
        auto now = chrono::steady_clock::now();
        chrono::duration<double> delta = now - last_time;
        last_time = now;
        player.update(delta.count());
        player.statis();
        cout << "[U] Upgrade garden | [B] Buy garden | [P] Pass | [Q] Quit\n";
        char choice;
        cin >> choice;
        if (choice == 'U' || choice == 'u'){
            int choice_garden;
            player.display_garden();
            cout << "Choose your garden: ";
            cin >> choice_garden;
            player.upgrade_garden(choice_garden - 1);
        }
        else if (choice == 'Q' || choice == 'q'){
            auto now = chrono::steady_clock::now();
            chrono::duration<double> delta = now - last_time;
            player.update(delta.count());
            player.save_game();
            break;
        }
        else if (choice == 'B' || choice == 'b'){
            cout << "Garden price: " << player.get_garden_cost() << "\n";
            player.buy_garden();
        }
        else{}
        this_thread::sleep_for(chrono::seconds(1));
    }
    return 0;
}