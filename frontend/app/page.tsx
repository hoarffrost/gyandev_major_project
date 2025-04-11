"use client"

import type React from "react"

import { useState, useRef, useEffect } from "react"
import { Send, Info, AlertTriangle } from "lucide-react"
import { Button } from "@/components/ui/button"
import ChatMessage from "@/components/chat-message"
import ScamInfoCard from "@/components/scam-info-card"
import { generateBotResponse } from "@/lib/chat-responses"

export default function Home() {
    const [messages, setMessages] = useState<Array<{ role: string; content: string; timestamp: Date }>>([
        {
            role: "bot",
            content:
                "👋 Hello! I'm ScamShield, your personal assistant for scam awareness in India. How can I help you today?\n\nTry asking about:\n- Common scams in India\n- How to prevent scams\n- What to do if you've been scammed",
            timestamp: new Date(),
        },
    ])
    const [inputMessage, setInputMessage] = useState("")
    const messagesEndRef = useRef<HTMLDivElement>(null)
    const [isTyping, setIsTyping] = useState(false)

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
    }

    useEffect(() => {
        scrollToBottom()
    }, [messages])

    const sendMessage = () => {
        if (inputMessage.trim() === "") return

        const userMessage = {
            role: "user",
            content: inputMessage,
            timestamp: new Date(),
        }

        setMessages((prev) => [...prev, userMessage])
        setInputMessage("")
        setIsTyping(true)

        // Simulate bot thinking
        setTimeout(() => {
            const botResponse = generateBotResponse(inputMessage)
            setMessages((prev) => [
                ...prev,
                {
                    role: "bot",
                    content: botResponse,
                    timestamp: new Date(),
                },
            ])
            setIsTyping(false)
        }, 1000)
    }

    const handleKeyPress = (e: React.KeyboardEvent) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault()
            sendMessage()
        }
    }

    return (
        <main className="flex min-h-screen flex-col items-center bg-gray-100">
            <div className="w-full max-w-md md:max-w-2xl mx-auto flex flex-col h-screen">
                {/* Header */}
                <header className="bg-green-600 text-white p-4 flex items-center gap-3">
                    <div className="w-10 h-10 rounded-full bg-white flex items-center justify-center">
                        {/* WhatsApp Logo SVG */}
                        <svg viewBox="0 0 32 32" className="w-6 h-6">
                            <path
                                fill="#25D366"
                                d="M16.004 0h-.008C7.174 0 0 7.176 0 16c0 3.472 1.12 6.7 3.022 9.316l-1.986 5.876 6.09-1.948A15.932 15.932 0 0016.004 32C24.83 32 32 24.822 32 16S24.83 0 16.004 0z"
                            />
                            <path
                                fill="#fff"
                                d="M25.314 22.62c-.386 1.09-1.918 1.992-3.14 2.256-.836.144-1.932.26-5.624-1.208-4.724-1.88-7.764-6.488-8-6.788-.226-.302-1.914-2.544-1.914-4.852 0-2.308 1.196-3.436 1.624-3.902.428-.466.936-.584 1.248-.584.302 0 .604 0 .872.016.28.016.654-.108.998.758.366.91 1.24 3.144 1.348 3.372.11.226.184.496.054.784-.13.29-.194.466-.386.73-.196.26-.406.584-.582.784-.194.226-.396.468-.168.916.226.448.998 1.916 2.148 3.106 1.476 1.54 2.688 2.032 3.07 2.256.38.226.604.184.826-.094s.964-1.124 1.222-1.512c.26-.386.52-.322.878-.196.36.13 2.28 1.072 2.668 1.268.39.196.654.292.748.448.92.156.92.902.534 1.992z"
                            />
                        </svg>
                    </div>
                    <div>
                        <h1 className="font-semibold text-lg">+91 9876543210</h1>
                        <p className="text-xs text-green-100">Active now</p>
                    </div>
                </header>

                {/* Chat container */}
                <div className="flex-1 overflow-y-auto bg-[#e5ddd5] p-4">
                    <div className="space-y-4">
                        {messages.map((message, index) => (
                            <ChatMessage key={index} role={message.role} content={message.content} timestamp={message.timestamp} />
                        ))}
                        {isTyping && (
                            <div className="flex items-center gap-2 text-gray-500 text-sm ml-2">
                                <div className="w-8 h-8 rounded-full bg-white flex items-center justify-center">
                                    {/* WhatsApp Logo for typing indicator */}
                                    <svg viewBox="0 0 32 32" className="w-4 h-4">
                                        <path
                                            fill="#25D366"
                                            d="M16.004 0h-.008C7.174 0 0 7.176 0 16c0 3.472 1.12 6.7 3.022 9.316l-1.986 5.876 6.09-1.948A15.932 15.932 0 0016.004 32C24.83 32 32 24.822 32 16S24.83 0 16.004 0z"
                                        />
                                        <path
                                            fill="#fff"
                                            d="M25.314 22.62c-.386 1.09-1.918 1.992-3.14 2.256-.836.144-1.932.26-5.624-1.208-4.724-1.88-7.764-6.488-8-6.788-.226-.302-1.914-2.544-1.914-4.852 0-2.308 1.196-3.436 1.624-3.902.428-.466.936-.584 1.248-.584.302 0 .604 0 .872.016.28.016.654-.108.998.758.366.91 1.24 3.144 1.348 3.372.11.226.184.496.054.784-.13.29-.194.466-.386.73-.196.26-.406.584-.582.784-.194.226-.396.468-.168.916.226.448.998 1.916 2.148 3.106 1.476 1.54 2.688 2.032 3.07 2.256.38.226.604.184.826-.094s.964-1.124 1.222-1.512c.26-.386.52-.322.878-.196.36.13 2.28 1.072 2.668 1.268.39.196.654.292.748.448.92.156.92.902.534 1.992z"
                                        />
                                    </svg>
                                </div>
                                <div className="bg-white rounded-lg px-3 py-2 shadow-sm">
                                    <div className="flex space-x-1">
                                        <div
                                            className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                                            style={{ animationDelay: "0s" }}
                                        ></div>
                                        <div
                                            className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                                            style={{ animationDelay: "0.2s" }}
                                        ></div>
                                        <div
                                            className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                                            style={{ animationDelay: "0.4s" }}
                                        ></div>
                                    </div>
                                </div>
                            </div>
                        )}
                        <div ref={messagesEndRef} />
                    </div>
                </div>

                {/* Scam Categories */}
                <div className="bg-white p-2 overflow-x-auto">
                    <div className="flex gap-2">
                        <Button
                            variant="outline"
                            size="sm"
                            className="whitespace-nowrap"
                            onClick={() => {
                                setInputMessage("Tell me about investment scams")
                                setTimeout(() => sendMessage(), 100)
                            }}
                        >
                            <AlertTriangle size={14} className="mr-1" /> Investment Scams
                        </Button>
                        <Button
                            variant="outline"
                            size="sm"
                            className="whitespace-nowrap"
                            onClick={() => {
                                setInputMessage("What are digital arrest scams?")
                                setTimeout(() => sendMessage(), 100)
                            }}
                        >
                            <AlertTriangle size={14} className="mr-1" /> Digital Arrest
                        </Button>
                        <Button
                            variant="outline"
                            size="sm"
                            className="whitespace-nowrap"
                            onClick={() => {
                                setInputMessage("How to prevent shopping scams?")
                                setTimeout(() => sendMessage(), 100)
                            }}
                        >
                            <AlertTriangle size={14} className="mr-1" /> Shopping Scams
                        </Button>
                        <Button
                            variant="outline"
                            size="sm"
                            className="whitespace-nowrap"
                            onClick={() => {
                                setInputMessage("What should I do if I've been scammed?")
                                setTimeout(() => sendMessage(), 100)
                            }}
                        >
                            <Info size={14} className="mr-1" /> If Scammed
                        </Button>
                    </div>
                </div>

                {/* Input area */}
                <div className="bg-white p-3 flex items-center gap-2">
                    <textarea
                        value={inputMessage}
                        onChange={(e) => setInputMessage(e.target.value)}
                        onKeyDown={handleKeyPress}
                        placeholder="Type a message"
                        className="flex-1 border rounded-lg px-3 py-2 focus:outline-none focus:ring-1 focus:ring-green-500 resize-none"
                        rows={1}
                    />
                    <Button onClick={sendMessage} size="icon" className="bg-green-600 hover:bg-green-700 rounded-full h-10 w-10">
                        <Send size={18} />
                    </Button>
                </div>
            </div>

            {/* Educational popup */}
            <div className="fixed bottom-4 right-4 md:block hidden">
                <ScamInfoCard />
            </div>
        </main>
    )
}
