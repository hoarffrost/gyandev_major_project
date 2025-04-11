"use client"

import { useState } from "react"
import { X, AlertTriangle, ChevronRight } from "lucide-react"
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from "@/components/ui/card"
import { Button } from "@/components/ui/button"

export default function ScamInfoCard() {
    const [isOpen, setIsOpen] = useState(true)

    if (!isOpen) {
        return (
            <Button onClick={() => setIsOpen(true)} className="bg-red-500 hover:bg-red-600 rounded-full h-12 w-12 shadow-lg">
                <AlertTriangle size={20} />
            </Button>
        )
    }

    return (
        <Card className="w-80 shadow-lg border-red-200">
            <CardHeader className="bg-red-50 pb-2">
                <div className="flex justify-between items-center">
                    <CardTitle className="text-red-700 flex items-center gap-2 text-lg">
                        <AlertTriangle size={18} />
                        Scam Alert
                    </CardTitle>
                    <Button variant="ghost" size="icon" onClick={() => setIsOpen(false)} className="h-8 w-8">
                        <X size={16} />
                    </Button>
                </div>
            </CardHeader>
            <CardContent className="pt-4">
                <div className="space-y-3 text-sm">
                    <p className="font-semibold">Did you know?</p>
                    <p>In 2024, Indians lost over ₹11,000 crore to digital scams, with an average daily loss of ₹60 crore.</p>
                    <div className="bg-yellow-50 p-2 rounded border border-yellow-200 text-xs">
                        <p className="font-medium text-yellow-800">Top Scams in India:</p>
                        <ul className="list-disc pl-4 mt-1 text-yellow-700 space-y-1">
                            <li>Investment Frauds (₹4,636 crore loss)</li>
                            <li>Digital Arrest Scams (₹1,616 crore loss)</li>
                            <li>Shopping Scams</li>
                        </ul>
                    </div>
                </div>
            </CardContent>
            <CardFooter className="pt-0">
                <Button
                    variant="link"
                    className="text-red-600 p-0 h-auto text-xs flex items-center"
                    onClick={() => {
                        window.open("https://www.cybercrime.gov.in/", "_blank")
                    }}
                >
                    Report scams on National Cyber Crime Portal
                    <ChevronRight size={12} />
                </Button>
            </CardFooter>
        </Card>
    )
}
