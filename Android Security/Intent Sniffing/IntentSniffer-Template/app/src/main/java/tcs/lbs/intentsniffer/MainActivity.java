package tcs.lbs.intentsniffer;

import androidx.appcompat.app.AppCompatActivity;

import android.content.IntentFilter;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    TextView LatitudeTextView, LongitudeTextView;
    static final String RECEIVER_ACTION = "tcs.lbs.locationapp.MainActivityReceiver";
//    static final String RECEIVER_ACTION = "tcs.lbs.weather_app.WeatherBroadcastReceiver";


    private MyLocationReceiver locationReceiver;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        LatitudeTextView = findViewById(R.id.LatitudeTextView);
        LongitudeTextView = findViewById(R.id.LongitudeTextView);

        locationReceiver = new MyLocationReceiver(LatitudeTextView, LongitudeTextView);
    }

    @Override
    protected void onResume() {
        super.onResume();
        IntentFilter filter = new IntentFilter();
        filter.addAction(RECEIVER_ACTION);
        registerReceiver(locationReceiver, filter);
    }

    @Override
    protected void onPause() {
        super.onPause();
        unregisterReceiver(locationReceiver);
    }
}
