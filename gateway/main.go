package main

import (
	"gateway/application"
	"gateway/infrastructure"
	"gateway/presentation"
	"log/slog"
	"net/http"
)

func main() {
	// Initialize Kafka producer
	producer := infrastructure.NewKafkaProducer("kafka:29092")

	// Initialize use case and handler
	messageUseCase := application.NewMessageUseCase(*producer)
	messageHandler := presentation.NewMessageHandler(messageUseCase)

	// Set up HTTP server and routes
	http.HandleFunc("/send", messageHandler.HandleSendMessage)

	slog.Info("Starting server on :8080")

	if err := http.ListenAndServe(":8080", nil); err != nil {
		slog.Error(err.Error())
	}
}
