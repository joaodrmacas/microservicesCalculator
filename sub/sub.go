package main

import (
	"bytes"
	"encoding/json"
	"net/http"
)

// RequestBody defines the structure of the request payload
type RequestBody struct {
	Number1 float64 `json:"number1"`
	Number2 float64 `json:"number2"`
}

// Response defines the structure of the response payload
type Response struct {
	Result float64 `json:"result"`
}

var DB_SERVICE_URL = "http://db-service:5006/save"

func main() {
	http.HandleFunc("/api/sub", subtractHandler)

	// Start the server on port 5000
	http.ListenAndServe(":5000", nil)
}

// subtractHandler handles the subtraction of two numbers
func subtractHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	var requestBody RequestBody

	// Decode the JSON request body
	err := json.NewDecoder(r.Body).Decode(&requestBody)
	if err != nil {
		http.Error(w, "Bad request", http.StatusBadRequest)
		return
	}

	// Perform the subtraction
	result := requestBody.Number1 - requestBody.Number2

	// Create the response
	response := Response{Result: result}

	// Set the response header to application/json
	w.Header().Set("Content-Type", "application/json")

	// Encode the response as JSON and write it to the response writer
	if err := json.NewEncoder(w).Encode(response); err != nil {
		http.Error(w, "Failed to encode response", http.StatusInternalServerError)
		return
	}

	// Prepare data for the external POST request
	saveData := map[string]interface{}{
		"result":    result,
		"operation": "subtraction",
	}

	// Convert saveData to JSON
	saveDataJSON, err := json.Marshal(saveData)
	if err != nil {
		http.Error(w, "Failed to create JSON payload", http.StatusInternalServerError)
		return
	}

	// Make a POST request to the db-service
	resp, err := http.Post(DB_SERVICE_URL, "application/json", bytes.NewBuffer(saveDataJSON))
	if err != nil {
		http.Error(w, "Failed to save to db-service", http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()

	// Optionally handle the response from the db-service (e.g., log it)
	if resp.StatusCode != http.StatusOK && resp.StatusCode != http.StatusCreated {
		http.Error(w, "Failed to save result", http.StatusInternalServerError)
	}
}
