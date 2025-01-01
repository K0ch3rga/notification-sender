package domain

type Message struct {
	Type    string `json:"Type"`
	Adress  string `json:"Address"`
	Title   string `json:"Title"`
	Message string `json:"Message"`
}
