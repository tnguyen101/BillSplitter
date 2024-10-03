#ifndef RECEIPT_H   // If MYCLASS_H is not defined
#define RECEIPT_H   // Define MYCLASS_H
#include <vector>

struct{std::string name, double price, bool more_than_one, std::vector<std::string> people} Item;

class Receipt {
private:
    std::vector<Item> items;
public:
    Receipt();      //
    void calculate_expenses();
    // remove and add recipt would go to receipt manager
    void add_person(std::string item_name, std::string person_name);// adds a person on the item to share
    void remove_person(std::string item_name, std:string person_name);// removes the person from the item
    bool get_state(std::string item_name);//gets whether one item or more items (0 for 1 item) (1 for 1+ items)
};

#endif  // End of include guard