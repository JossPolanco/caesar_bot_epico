const { Client, LocalAuth, MessageMedia } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

const client = new Client({
    authStrategy: new LocalAuth()
});

client.on('qr', (qr) => {
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.on("message", async (message) => {
   const chat = await message.getChat();

    if (message.body.toLowerCase() === 'ping') {
        await message.reply('pong');
    } else if (message.body.toLowerCase() === 'que') {
        const url = 
            "https://images7.memedroid.com/images/UPLOADED574/625f4dd6290b4.jpeg";
        try { 
            const media = await MessageMedia.fromUrl(url);
            await client.sendMessage(message.from, media, {
                sendMediaAsSticker: true,
                stickerAuthor: "yo",
                stickerName: "sticker"
            });
        } catch (error) {
            console.error('Error sending sticker:', error);
        }
    }
}); 
client.initialize();