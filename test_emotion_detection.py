from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):

        # Test result for joy Dominant Emotion
        response_1 = emotion_detector("I am glad this happened")
        self.assertEqual(response_1['dominant_emotion'], 'joy')

        # Test result for anger Dominant Emotion
        response_2 = emotion_detector("I am really mad about this")
        self.assertEqual(response_2['dominant_emotion'], 'anger')

        # Test result for disgust Dominant Emotion
        response_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response_3['dominant_emotion'], 'disgust')

        # Test result for sadness Dominant Emotion
        response_4 = emotion_detector("I am so sad about this")
        self.assertEqual(response_4['dominant_emotion'], 'sadness')

        # Test result for fear Dominant Emotion
        response_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(response_5['dominant_emotion'], 'fear')

# Call the unit tests
unittest.main()