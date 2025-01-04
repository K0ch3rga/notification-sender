package presentation

import (
	"encoding/json"
	"gateway/application"
	"gateway/domain"
	"net/http"
)

type MessageHandler struct {
	useCase *application.MessageUseCase
}

func NewMessageHandler(useCase *application.MessageUseCase) *MessageHandler {
	return &MessageHandler{useCase: useCase}
}

func (h *MessageHandler) HandleSendMessage(w http.ResponseWriter, r *http.Request) {
	var msg domain.Message
	if err := json.NewDecoder(r.Body).Decode(&msg); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	if err := h.useCase.SendMessage(msg); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusAccepted)
}
