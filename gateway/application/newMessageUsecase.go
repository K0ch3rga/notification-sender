package application

import (
	"encoding/json"
	"gateway/domain"
	"gateway/infrastructure"
	"log/slog"
)

type MessageUseCase struct {
	producer infrastructure.KafkaProducer
}

func NewMessageUseCase(producer infrastructure.KafkaProducer) *MessageUseCase {
	return &MessageUseCase{producer: producer}
}

func (uc *MessageUseCase) SendMessage(msg domain.Message) error {
	data, err := json.Marshal(msg)
	slog.Info(string(data))
	if err != nil {
		return err
	}
	return uc.producer.Produce(msg.Type, string(data))
}
