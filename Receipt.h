#ifndef RECEIPT_H   // If MYCLASS_H is not defined
#define RECEIPT_H   // Define MYCLASS_H
#include <vector>

class Receipt {
private:
    struct{std::string name, double price, std::vector<std::string> name} Item;
public:
    Receipt();      // Constructor
    void add_receipt();
    void calculate_expenses();
    void remove_receipt();
};

#endif  // End of include guard