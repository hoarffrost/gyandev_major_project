import { User, Bot } from "lucide-react"
import { formatDistanceToNow } from "date-fns"

interface ChatMessageProps {
    role: string
    content: string
    timestamp: Date
}

export default function ChatMessage({ role, content, timestamp }: ChatMessageProps) {
    const isUser = role === "user"

    return (
        <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
            {!isUser && (
                <div className="w-8 h-8 rounded-full bg-green-600 flex items-center justify-center mr-2">
                    <Bot size={16} className="text-white" />
                </div>
            )}
            <div
                className={`max-w-[80%] rounded-lg px-3 py-2 shadow-sm ${isUser ? "bg-green-100 text-green-900" : "bg-white text-gray-800"
                    }`}
            >
                <div className="whitespace-pre-wrap">{content}</div>
                <div className="text-xs mt-1 text-gray-500">{formatDistanceToNow(timestamp, { addSuffix: true })}</div>
            </div>
            {isUser && (
                <div className="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center ml-2">
                    <User size={16} className="text-gray-600" />
                </div>
            )}
        </div>
    )
}
