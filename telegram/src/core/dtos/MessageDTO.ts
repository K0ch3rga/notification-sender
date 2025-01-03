export class MessageDTO {
    type: "email" | "telegram" | "push";
    address: string;
    title: string;
    message: string;

    constructor(type: 'email' | 'telegram' | 'push', address: string, title: string, message: string) {
        this.type = type;
        this.address = address;
        this.title = title;
        this.message = message;
    }
}
