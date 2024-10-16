package main

import (
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
	json.NewEncoder(w).Encode(response)
}
