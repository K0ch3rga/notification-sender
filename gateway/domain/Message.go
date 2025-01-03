package domain

type Message struct {
	Type    string `json:"type"`
	Adress  string `json:"address"`
	Title   string `json:"title"`
	Message string `json:"message"`
}
