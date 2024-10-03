#include <iostream>
#include <fstream>
#include <curl/curl.h>
#include "json.hpp"  // nlohmann JSON library

using json = nlohmann::json;

// Function to write data from libcurl response to a string
size_t WriteCallback(void* contents, size_t size, size_t nmemb, std::string* userp) {
    userp->append((char*)contents, size * nmemb);
    return size * nmemb;
}

// Function to fetch JSON data from GitHub
std::string fetchJSONFile(const std::string& url) {
    CURL* curl;
    CURLcode res;
    std::string readBuffer;

    curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);
        res = curl_easy_perform(curl);
        if (res != CURLE_OK) {
            std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
        }
        curl_easy_cleanup(curl);
    }
    return readBuffer;
}

int main() {
    // URL of the JSON file in your GitHub repository
    std::string url = "https://raw.githubusercontent.com/your-username/your-repo/main/data.json";

    // Fetch the JSON data
    std::string jsonData = fetchJSONFile(url);

    // Check if data is fetched
    if (jsonData.empty()) {
        std::cerr << "Failed to fetch data from GitHub!" << std::endl;
        return 1;
    }

    // Parse the JSON data using nlohmann/json
    try {
        auto jsonParsed = json::parse(jsonData);

        // Example: Print the JSON data
        std::cout << "Fetched and parsed JSON data:\n" << jsonParsed.dump(4) << std::endl;

        // Accessing data: if the JSON contains a list of users, for example
        if (jsonParsed.contains("users")) {
            for (const auto& user : jsonParsed["users"]) {
                std::cout << "Name: " << user["name"] << ", Email: " << user["email"] << std::endl;
            }
        }
    } catch (json::parse_error& e) {
        std::cerr << "Failed to parse JSON: " << e.what() << std::endl;
    }

    return 0;
}