#include "Receipt.h"

void Receipt::remove_person(std::string item_name, std::string person_name) {
    bool found(false)
    bool item_found(false)
    for (auto item = items.begin(); item != items.end(); item++) {
        if(item.name == item_name) {
            item_found = true;
            for(auto person = item.people.begin(); person != item.people.end(); person++) {
                if(person == person_name) {
                    item.people.erase(person)
                    found = true;
                    break;
                }
            }
        }
        if(item_found) break;
    }
    if(!found) std::cout << "Person is not found in this Item";
    else if(!item_found) std::cout << "Item not found";
}

void Receipt::add_person(std::string item_name, std::string person_name) {
    bool found(false);
    bool item_found(false);
    auto item = items.begin()
    while (item != items.end()) {
        if(item.name == item_name) {
            item_found = true;
            for(auto person = item.people.begin(); person != item.people.end(); person++) {
                if(person == person_name) {
                    found = true;
                    break;
                }
            }
        }
        if (item_found) break;
    }
    if(found) {
        std::cout "person is already with the Item";
    } else if(!item_found) {
        std::cout << "Item not found";
    } else {
        item.people.push_back(person_name);
    }
}